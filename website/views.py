from datetime import datetime
import json
from django.shortcuts import render, redirect,HttpResponse
from .models import  Utility_data, Order_data,Transport_data, Warehouse_data
from django.contrib.auth.models import User,auth
import qrcode
from io  import BytesIO
import qrcode.image.svg
import base64
def home(request):
    if request.user.is_authenticated:
        _type = Utility_data.objects.get(email=request.user.username)._type
        if _type == 'local-warehouse' or _type == 'inter-warehouse':
            return render(request, 'warehouse.html')
        if _type == 'large-goodscarrier' or _type == 'small-goodscarrier' or _type == 'moto-goodscarrier':
            return render(request, 'transport.html')
        if _type=="seller":
            return render(request, 'seller.html')
    else:
        return redirect('/login')
    
def register(request):
    return render(request, 'register.html')

def register_user(request):
    _name = request.POST['name']
    _email = request.POST['email']
    _mobile = request.POST['mobile']
    _type = request.POST['type']
    _password = request.POST['password']
    Utility_data(name=_name, email=_email, mobile=_mobile, _type=_type).save()
    user = User.objects.create_user(first_name = _name,username=_email,password=_password)
    user.save()
    return redirect('/')

def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    return render(request, 'login.html')

def login_user(request):
    _email = request.POST['email']
    _password = request.POST['password']
    user = auth.authenticate(request,username=_email, password=_password)
    if user is not None:
        auth.login(request, user)
        return redirect('/')
    else:
        return redirect('/login')
    
def logout_user(request):
    auth.logout(request)
    return redirect('/')

def generate_order(request):
    _name = request.POST['name']
    _email = request.POST['email']
    _from = request.POST['from']
    _to = request.POST['to']
    _size = request.POST['size']
    _weight = request.POST['weight']
    _time = datetime.now().strftime("%d/%m/%Y %H:%M:%S:%f")
    _orderid = str(_time).replace('/','').replace(' ','').replace(':','')+str(_email).split('@')[0]
    _status = 'packed'
    _current_location = Utility_data.objects.get(email=request.user.username)._type
    _status_log = json.dumps({"_logs":[{'time':_time,'status':'packed','loc':_current_location+" "+_from}]})
    print(_name,_email,_from,_to,_size,_weight,_time,_orderid,_status,_status_log,_current_location)
    order_obj = Order_data.objects.create(_name=_name,_email=_email,_from=_from,_to=_to,_size=_size,_weight=_weight,_time=_time,_orderid=_orderid,_status=_status,_status_log=_status_log,_current_location=_current_location)
    order_obj.save()
    
    #Qr code generation
    img = qrcode.make(_orderid)
    buffer = BytesIO()
    img.save(buffer)
    img = buffer.getvalue()
    img_base64 =  base64.b64encode(img).decode('utf-8')
    html_base = '<html><body><h3>Order ID: '+_orderid+'</h3> <h3>From :'+_from+'</h3> <h3>To :'+_to+'</h3> <h3>Size :'+_size+'</h3> <h3>Weight :'+_weight+'</h3> <h3>Time :'+_time+'</h3> <h3>Status :'+_status+'</h3> <h3>Current Location :'+_current_location+'</h3> <img src="data:image/png;base64,{}" alt="QR Code" /> </body></html>'.format(img_base64)
    return HttpResponse(html_base)

def transport(request):
    if request.user.is_authenticated :
        _type = Utility_data.objects.get(email=request.user.username)._type
        if _type == 'large-goodscarrier' or _type == 'small-goodscarrier' or _type == 'moto-goodscarrier':
            return render(request, 'transport.html')
        return HttpResponse('You are not authorized to access this page')
    return HttpResponse('Login to access this page')

def transport_order(request):
    _orderid = request.POST['orderid']
    _from = Order_data.objects.get(_orderid=_orderid)._current_location
    _to = Order_data.objects.get(_orderid=_orderid)._to
    _time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    _status = Order_data.objects.get(_orderid=_orderid)._status
    if(_status == 'inwarehouse'):
        w_obj = Warehouse_data.objects.get(_orderid=_orderid,_status='inwarehouse')
        w_obj._status = 'leftwarehouse'
        w_obj._time = _time
        w_obj.save()
        _status = 'transporting'
        Transport_data.objects.create(_orderid=_orderid,_from=_from,_to=_to,_time=_time,_status=_status).save()
        order_obj = Order_data.objects.get(_orderid=_orderid)
        order_obj._status = _status
        order_obj._current_location = Utility_data.objects.get(email=request.user.username)._type
        _s_log = json.loads(order_obj._status_log)
        _s_log['_logs'].append({'time':_time,'status':_status,'loc':order_obj._current_location+" "+_from})
        order_obj._status_log = json.dumps(_s_log)
        order_obj.save()
        return HttpResponse('Status updated')
    if(_status == 'packed'):
        _status = 'transporting'
        Transport_data.objects.create(_orderid=_orderid,_from=_from,_to=_to,_time=_time,_status=_status).save()
        order_obj = Order_data.objects.get(_orderid=_orderid)
        order_obj._status = _status
        order_obj._current_location = Utility_data.objects.get(email=request.user.username)._type
        _s_log = json.loads(order_obj._status_log)
        _s_log['_logs'].append({'time':_time,'status':_status,'loc':order_obj._current_location+" "+_from})
        order_obj._status_log = json.dumps(_s_log)
        order_obj.save()
        return HttpResponse('Status updated')
    return HttpResponse('Status not updated')

def warehouse(request):
    if request.user.is_authenticated :
        _type = Utility_data.objects.get(email=request.user.username)._type
        if _type == 'local-warehouse' or _type == 'inter-warehouse':
            return render(request, 'warehouse.html')
        return HttpResponse('You are not authorized to access this page')
    return HttpResponse('Please login to access this page')

def warehouse_log(request):
    _orderid = request.POST['orderid']
    _status = Order_data.objects.get(_orderid=_orderid)._status
    _time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    _loc = Utility_data.objects.get(email=request.user.username)._type
    if _status == "transporting":
        Transport_data.objects.get(_orderid=_orderid).delete()
        order_obj = Order_data.objects.get(_orderid=_orderid)
        order_obj._status = 'inwarehouse'
        order_obj._current_location = _loc
        _s_log = json.loads(order_obj._status_log)
        _s_log['_logs'].append({'time':_time,'status':'inwarehouse','loc':_loc})
        order_obj._status_log = json.dumps(_s_log)
        order_obj.save()
        Warehouse_data.objects.create(_orderid=_orderid,_time=_time,_status="inwarehouse").save()
        return HttpResponse('Status updated')
    return HttpResponse('Status not updated')

def delivery(request):
    return render(request, 'delivery.html')

def out_delivery(request):
    _orderid = request.POST['orderid']
    _status = Order_data.objects.get(_orderid=_orderid)._status
    _time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    _loc = Utility_data.objects.get(email=request.user.username)._type
    if _status == "transporting":
        Transport_data.objects.get(_orderid=_orderid).delete()
        order_obj = Order_data.objects.get(_orderid=_orderid)
        order_obj._status = 'Delivered'
        order_obj._current_location = _loc
        _s_log = json.loads(order_obj._status_log)
        _s_log['_logs'].append({'time':_time,'status':'Delivered','loc':_loc})
        order_obj._status_log = json.dumps(_s_log)
        order_obj.save()
        return HttpResponse('Status updated')
    return HttpResponse('Status not updated')

def track(request):
    return render(request, 'track.html')
def track_order(request):
    _orderid = request.POST['orderid']
    _s_log = Order_data.objects.get(_orderid=_orderid)._status_log
    _s_log = json.loads(_s_log)
    _s_log = _s_log['_logs']
    ih="<table>"
    def get_row(log):
        return "<tr><td>"+log['time']+"</td><td>"+log['status']+"</td><td>"+log['loc']+"</td></tr>"
    for log in _s_log:
        ih += get_row(log)
    ih += "</table>"
    return HttpResponse(ih)
