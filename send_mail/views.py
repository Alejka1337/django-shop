from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponseRedirect
from django.template import loader


def mail_send(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    message = request.POST.get('message')
    phone = request.POST.get('Phone')

    template = loader.get_template('send_email/contact_form.txt')
    context = {
        'name': name,
        'email': email,
        'message': message,
        'Phone': phone,

    }
    message = template.render(context)

    email = EmailMultiAlternatives(
        "Обращение от клиента", message,
        "Hello" + "- Lucky Man !",
        ["m.blinov@tavriav.com.ua"]

    )

    email.content_subtype = 'html'
    email.send()
    messages.success(request, 'Message sent seccessfully !')

    return HttpResponseRedirect('feedback/')
