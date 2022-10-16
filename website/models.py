from django.db import models

    
class Utility_data(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.IntegerField(max_length=10)
    email = models.EmailField(max_length=50)
    _type = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Order_data(models.Model):
    _name = models.CharField(max_length=50)
    _email = models.EmailField(max_length=50)
    _from = models.CharField(max_length=50)
    _to = models.CharField(max_length=50)
    _size = models.CharField(max_length=50)
    _weight = models.CharField(max_length=50)
    _time = models.CharField(max_length=50)
    _orderid = models.CharField(max_length=50)
    _status = models.CharField(max_length=50)
    _status_log = models.CharField(max_length=500)
    _current_location = models.CharField(max_length=50)

    def __str__(self):
        return self._orderid

class Transport_data(models.Model):
    _orderid = models.CharField(max_length=50)
    _from = models.CharField(max_length=50)
    _to = models.CharField(max_length=50)
    _time = models.CharField(max_length=50)
    _status = models.CharField(max_length=50)
    def __str__(self):
        return self._orderid
    
class Warehouse_data(models.Model):
    _orderid = models.CharField(max_length=50)
    _status = models.CharField(max_length=50)
    _time = models.CharField(max_length=50)
    #s_wmail = models.EmailField(max_length=50)
    def __str__(self):
        return self._orderid
     
    