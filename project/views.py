from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def home(request):
    if request.method == 'POST':
        Fullname = request.POST['Fullname']
        Phonenumber = request.POST['Phone']
        Email = request.POST['Email']
        Subject = request.POST['Subject']
        Message = request.POST['Message']

        # send email
        send_mail(
            Subject,
            "From: "+ Fullname + " \n\n "+ "Phone Number: "+ Phonenumber +" \n\n  "+"Subject: " + Subject + " \n\n\n" + Message + "\n\n"+"Thank You,"+"\n\n\n"+ "@ Expanse Products Ltd",#message
            Email,# from 
            [settings.EMAIL_HOST_USER,],#to email
        )

        return render(request,'home.html',{'Message':Message,'Email':Email,'Fullname':Fullname,'Phonenumber':Phonenumber,"Subject":Subject})
    else:
        return render(request,'index.html')