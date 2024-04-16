from django.core.mail import send_mail, mail_admins, BadHeaderError
from django.shortcuts import render


def say_hello(request):
    try:
        mail_admins('subject', 'message', html_message='message')
        send_mail('subject', 'message', 'lcramer@tandemdiabetes.com', [''])
    except BadHeaderError:
        pass
    return render(request, 'hello.html', {'name': 'Mosh'})
