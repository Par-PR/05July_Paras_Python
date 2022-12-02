from django.shortcuts import render, redirect
from .forms import SignupForm,notesForm,updateForm
from .models import Signup
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.core.mail import send_mail
from batchproject import settings
import random
import requests

# Create your views here.

def index(request):
    if request.method=='POST': #root
        if request.POST.get('signup')=='signup':
            username=""
            newuser=SignupForm(request.POST)
            if newuser.is_valid():
                username=newuser.cleaned_data.get("username")
                try:
                    un=Signup.objects.get(username=username)
                    print("Username is already exists!")
                    messages.error(request,"Username is already exists!")
                except Signup.DoesNotExist:
                    newuser.save()
                    print("Signup successfully!")

                    # Email Sending
                    otp=random.randint(1111,9999)
                    sub='Welcome!'
                    msg=f'Hello User!\nWelcome to NotesApp\n\nYour account has been created with us.\nEnjoy our services.\nYour one time password: {otp}\nNeed any help...\n+91 9724799469 | sanket.tops@gmail.com'
                    from_ID=settings.EMAIL_HOST_USER
                    to_ID=['paraspethani12@gmail.com']
                    #to_ID=[request.POST['username']]
                    send_mail(subject=sub,message=msg,from_email=from_ID,recipient_list=to_ID)
                    
                    messages.info(request,"Signup successfully!")
                    return redirect('notes')
            else:
                print(newuser.errors)
                messages.error(request,"Error! Something wen wrong...Try after some time.")
        elif request.POST.get('signin')=='signin':
            unm=request.POST['username']
            pas=request.POST['password']

            user=Signup.objects.filter(username=unm,password=pas)
            uid=Signup.objects.get(username=unm)
            print("Username:",uid)
            print("UserID:",uid.id)
            if user: #true
                print("Login Successfully!")
                request.session['user']=unm #session creation
                request.session['uid']=uid.id

                return redirect('notes')
            else:
                print("Error! Username or Password does not match.") 
                messages.error(request,"Error! Username or Password does not match.")   
    return render(request,'index.html')

def notes(request):
    user=request.session.get('user')
    if request.method=='POST':
        mynote=notesForm(request.POST,request.FILES)
        if mynote.is_valid():
            mynote.save()
            print("Your notes has been submitted!")
        else:
            print(mynote.errors)
    return render(request,'notes.html',{'cuser':user})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def profile(request):
    user=request.session.get('user')
    uid=request.session.get('uid')
    cid=Signup.objects.get(id=uid)
    if request.method=='POST':
        updatefrm=updateForm(request.POST)
        if updatefrm.is_valid():
            updatefrm=updateForm(request.POST,instance=cid)
            updatefrm.save()
            print("Your profile has been updated!")
            return redirect('notes')
        else:
            print(updatefrm.errors)
    return render(request,'profile.html',{'cid':Signup.objects.get(id=uid),'cuser':user})

def userlogout(request):
    logout(request)
    return redirect("/")
