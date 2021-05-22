from django.shortcuts import render
from EmailModule.settings import EMAIL_HOST_USER
from . import forms
from django.core.mail import send_mail
# Create your views here.
#DataFlair #Send Email
def subscribe(request):
    sub = forms.Subscribe()
    if request.method == 'POST':
        sub = forms.Subscribe(request.POST)
        subject = 'Welcome to Anirudh NewsLetter '
        message = 'Thank you for subscribing to us, we will be sending you important information regularly'
        recepient = str(sub['Email'].value())
        send_mail(subject, 
            message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        data = {'recepient': recepient}
        return render(request, 'subscribe/success.html', data)
    return render(request, 'subscribe/index.html', {'form':sub})