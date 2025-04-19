from django.contrib import admin
from .models import Order # 导入你的模型

# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('strCode', 'playMethod', 'drawTime', 'saleTime', 'price', 'machineId', 'activity') # 选择你想在列表页显示的字段
    list_filter = ('activity', 'playMethod', 'drawTime') # 添加过滤器
    search_fields = ('strCode', 'serialNumber', 'machineId', 'storeAddress') # 添加搜索字段