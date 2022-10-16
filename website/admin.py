from django.contrib import admin
from .models import Utility_data, Order_data, Transport_data, Warehouse_data
# Register your models here.
admin.site.register(Utility_data)
admin.site.register(Order_data)
admin.site.register(Transport_data)
admin.site.register(Warehouse_data)