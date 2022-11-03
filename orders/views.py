from django.shortcuts import render, redirect
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import CartLogic
from ecomm.models import Product
from .liqpay_controller import LiqpayChekout, LiqpayCallback


def order_create(request):
    cart = CartLogic(request)

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()

            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            return redirect('/orders/created')

    else:
        form = OrderCreateForm

    return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})


def order_created(request):
    cart = CartLogic(request)
    total_price = int(cart.get_total_price())

    liqpay = LiqpayChekout(total_price)
    liqpay.set_order_id()
    data = liqpay.create_param_checkout()[0]
    signature = liqpay.create_param_checkout()[1]

    return render(request, 'orders/order/created.html', {'data': data, 'signature': signature})


def thanks_page(request):
    cart = request.session['cart']

    liqpay = LiqpayCallback()
    res = liqpay.send_request()
    status = liqpay.get_response_status(res)

    if status != 'success':
        status_error = True

        return render(request, 'orders/order/thanks.html', {"status": status_error})

    else:

        request.session['cart'] = {}
        request.session['counter_items'] = 0

        for key, value in cart.items():
            product = Product.objects.get(pk=key)
            product.quantity -= value['quantity']
            product.save()

        order = Order.objects.order_by('-id')[:1].get()
        order.paid = True
        order.save()

    return render(request, 'orders/order/thanks.html')



