from django.shortcuts import render
from django.http import HttpResponse
from  .models import  Delivery_Utilities
# Create your views here.
def home(request):
    return HttpResponse("Hello World")
    
def register(request):
    objs = Delivery_Utilities.objects.all()
    for obj in objs:
        print(obj.name,obj.email,obj.mobile,obj.type,obj.password)
    return render(request,'register.html')

def register_user(request):
    
    _name = request.POST['name']
    _email = request.POST['email']
    _mobile = request.POST['mobile']
    _type = request.POST['type']
    _password = request.POST['password']
    _password2 = request.POST['password2']
    obj = Delivery_Utilities.objects.create(name=_name,email=_email,mobile=_mobile,type=_type,password=_password)
    obj.save()
    return HttpResponse("Register User")

def login(request):
    return render(request,'login.html')
    
def login_user(request):
    _email = request.POST['email']
    _password = request.POST['password']
    
    obj = Delivery_Utilities.objects.filter(email=_email,password=_password)
    if obj:
        print(obj[0].type)
        if (obj[0].type == 'WareHouse'):
            return render(request,'warehouse.html')
        if (obj[0].type == 'Two Wheeler'):
            return render(request,'twowheeler.html')
        if (obj[0].type == 'Four Wheeler'):
            return render(request,'fourwheeler.html')
        return HttpResponse("Login Success")
    else:
        return HttpResponse("Login Failed")
    #return HttpResponse("Login User")