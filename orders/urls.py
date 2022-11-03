from django.urls import re_path, path
from . import views


urlpatterns = [
    # re_path(r'^create/$', views.order_create, name='order_create'),
    path('create/', views.order_create, name='order_create'),
    path('created/', views.order_created, name='order_created'),
    path('thanks/', views.thanks_page, name='thanks_page'),
]