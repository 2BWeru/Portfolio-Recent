from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def home(request):
    # if request.method == 'POST':
    #     name = request.POST['name']
    #     email = request.POST['email']
    #     message = request.POST['message']

    #     # send email
    #     send_mail(
    #         name,
    #         email,# from 
    #         message,
    #         [settings.EMAIL_HOST_USER,],#to email
    #     )

    #     return render(request,'home.html',{'message':message,'email':email,'name':name})
    # else:
        return render(request,'index.html')