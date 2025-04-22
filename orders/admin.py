from django.contrib import admin, messages
from django.utils import timezone
from datetime import datetime
from django.urls import path, reverse
from django.http import HttpResponseRedirect, JsonResponse
from .models import Order
import json
# class SaleDateListFilter(admin.SimpleListFilter):
#     """
#     自定义过滤器，允许按 saleTime 字符串字段的日期部分过滤：今天 或 昨天及之前。
#     """
#     title = '销售日期'
#     parameter_name = 'sale_date'

#     def lookups(self, request, model_admin):
#         return (
#             ('today', '今天'),
#             ('before_today', '昨天及之前'),
#         )

#     def queryset(self, request, queryset):
#         now = timezone.now()
#         value = self.value()
#         today_str = now.strftime('%Y/%m/%d')

#         if value == 'today':
#             return queryset.filter(saleTime__startswith=today_str)
#         if value == 'before_today':
#             return queryset.filter(saleTime__lt=f"{today_str}-00:00:00")
#         return queryset

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('strCode', 'playMethod', 'drawTime', 'saleTime', 'price', 'machineId', 'activity')
    # list_filter = ('activity', 'playMethod', 'drawTime', SaleDateListFilter)
    search_fields = ('strCode', 'serialNumber', 'machineId', 'storeAddress')
    actions = []

    def delete_orders_by_date(self, request):
        """
        自定义视图，用于根据日期范围批量删除订单。
        """
        if request.method == 'POST':
            try:
                # 解析 JSON 数据
                data = json.loads(request.body)
                start_date = data.get('start_date')
                end_date = data.get('end_date')

                if not start_date or not end_date:
                    return JsonResponse({'status': 'error', 'message': '请提供开始日期和结束日期'}, status=400)

                # 将日期字符串转换为日期对象
                start_date_obj = datetime.strptime(start_date, '%Y-%m-%d')
                end_date_obj = datetime.strptime(end_date, '%Y-%m-%d')

                # 格式化为字符串以匹配 saleTime 格式
                start_date_str = start_date_obj.strftime('%Y/%m/%d')
                end_date_str = end_date_obj.strftime('%Y/%m/%d')

                # 筛选并删除订单
                orders_to_delete = Order.objects.filter(
                    saleTime__gte=f"{start_date_str}-00:00:00",
                    saleTime__lte=f"{end_date_str}-23:59:59"
                )
                count, _ = orders_to_delete.delete()

                return JsonResponse({'status': 'success', 'message': f'成功删除了 {count} 条订单'})

            except json.JSONDecodeError:
                return JsonResponse({'status': 'error', 'message': '请求数据格式错误'}, status=400)
            except Exception as e:
                return JsonResponse({'status': 'error', 'message': f'发生错误: {str(e)}'}, status=500)

        return JsonResponse({'status': 'error', 'message': '仅支持 POST 请求'}, status=405)

    # 添加自定义 URL
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                'delete-by-date/',
                self.admin_site.admin_view(self.delete_orders_by_date),
                name='orders_delete_by_date'
            ),
        ]
        return custom_urls + urls