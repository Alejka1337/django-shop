from django.urls import path

import send_mail
from send_mail.views import mail_send

app_name = 'send_mail'

urlpatterns = [
    path('send_mail', send_mail.views.mail_send, name='send_mail'),
]