
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import logout as logouts
from app1.models import Table1,Image
from.forms import RegisterForm,LoginForm,UpdateForm,ChangePasswordForm,ImageForm
from django.contrib import messages
# Create your views here.
def hello(request):
    return HttpResponse("welcome to django")
def index(request):
    return render(request,'index.html')  
def index(request):
    rst=45
    return render(request,"index.html",{'data':rst})   
# def register(request):
#     if request.method=='POST':
#         form=RegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request,"data saved")
#             return redirect('/')
#     else:
#         form=RegisterForm()
#     return render(request,"register.html",{'data':form})   
# 

def register(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data['name']
            uage=form.cleaned_data['age']
            uemail=form.cleaned_data['email']
            uplace=form.cleaned_data['place']
            upassword=form.cleaned_data['password']
            cpassword=form.cleaned_data['cpassword']

            user=Table1.objects.filter(email=uemail).exists()

            if user:
                messages.warning(request,"email already existing")
                return redirect('/register')
            elif upassword!=cpassword:
                messages.warning(request,"password mismatch")
                return redirect('/register')
            else:
                tab=Table1(name=uname,age=uage,email=uemail,place=uplace,password=upassword)
                tab.save()
                messages.success(request,"data saved")
                return redirect('/')
    else:
        form=RegisterForm()
    return render(request,"register.html",{'data':form})   

def login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            uemail=form.cleaned_data['email']
            upassword=form.cleaned_data['password']

            user=Table1.objects.get(email=uemail)

            if not user:
                messages.warning(request,"email does not existing")
                return redirect('/login')
            elif upassword!=user.password:
                messages.warning(request,"password incorrect")
                return redirect('/login')
            else:
                messages.success(request,"login success")
                return redirect('/home/%s' % user.id )
    else:
        form=LoginForm()
    return render(request,"login.html",{'data':form})   
def home(request,id):
    user=Table1.objects.get(id=id)
    return render(request,"home.html",{'data':user})

def update(request,id):
    user=Table1.objects.get(id=id)
    if request.method=='POST':
        form=UpdateForm(request.POST or None,instance=user)
        if form.is_valid():
            form.save()
            messages.success(request,"data updated")
            return redirect('/home/%s' % user.id)
    else:
        form=UpdateForm(instance=user)
    return render(request,"update.html",{'form':form,'user':user})   

def changepass(request,id):
    user=Table1.objects.get(id=id)
    if request.method=='POST':
        form=ChangePasswordForm(request.POST)
        if form.is_valid():
            opassword=form.cleaned_data['oldpassword']
            npassword=form.cleaned_data['newpassword']
            cpassword=form.cleaned_data['cpassword']

            if user.password!=opassword:
                messages.warning(request,"incorrect pass")
                return redirect('/changepass')
            elif opassword==npassword:
                messages.warning(request,"password looks similar")
                return redirect('/changepass')
            elif npassword!=cpassword:
                messages.warning(request,"password mismatch")
                return redirect('/changepass')
            else:
                user.password=npassword
                user.save()
                messages.success(request,"data changed")
                return redirect('/home/%s' % user.id)
    else:
        form=ChangePasswordForm()
    return render(request,"changepass.html",{'form':form,'user':user})   

def logout(request):
    logouts(request)
    messages.success(request,"logouts successfull")
    return redirect('/')

def image(request):
    if request.method=='POST':
        form=ImageForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            name=form.cleaned_data['Name']
            age=form.cleaned_data['Age']
            email=form.cleaned_data['Email']
            photo=form.cleaned_data['Photo']
            place=form.cleaned_data['Place']
            password=form.cleaned_data['Password']
            cpassword=form.cleaned_data['Cpassword']

            user=Image.objects.filter(Email=email).exists()

            if user:
                messages.warning(request,"email already existing")
                return redirect('/image')
            elif password!=cpassword:
                messages.warning(request,"password mismatch")
                return redirect('/image')
            else:
                tab=Image(Name=name,Age=age,Email=email,Place=place,Password=password,Photo=photo)
                tab.save()
                messages.success(request,"data saved")
                return redirect('/')
    else:
        form=ImageForm()
    return render(request,"register2.html",{'data':form})   

