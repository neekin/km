from django.contrib import admin
from django.urls import path, reverse
from django.shortcuts import redirect
from django.utils.html import format_html
import uuid
from .models import Licence
# Register your models here.
@admin.register(Licence)
class LicenceAdmin(admin.ModelAdmin):
    list_display = ("machine_code","type","remark","status_display","type_button")
    
    def type_button(self, obj):
        """在列表里显示按钮：若启用则显示“禁用”，若停用则显示“启用”"""
        if obj.enabled == 1:
            return format_html(
                '<a type="button" class="el-button stop-submit el-button--danger el-button--small" data-name="delete_selected" href="{}"><span style="color:white">禁用</span></a>',
                reverse("admin:licence_licence_toggle_enabled", args=[obj.pk])
            )
        else:
            return format_html(
                '<a type="button" class="el-button el-button--primary el-button--small" data-name="add_item" href="{}"><span style="color:white">启用</span></a>',
                reverse("admin:licence_licence_toggle_enabled", args=[obj.pk])
            )
    type_button.short_description = "操作"

    def status_display(self, obj):
        """给状态添加样式"""
        if obj.status == 1:  # 在线
            return format_html('<span class="el-tag el-tag--light">在线</span>')
        else:  # 离线
            return format_html('<span class="el-tag el-tag--danger el-tag--light">离线</span>')
    status_display.short_description = "机器状态"

    def has_add_permission(self,request):
      return False
    def get_urls(self):
        """定义自定义URL，用于切换enabled值"""
        urls = super().get_urls()
        custom_urls = [
            path(
                "<int:pk>/toggle_enabled/",  # 注意这里更改了顺序
                self.admin_site.admin_view(self.toggle_enabled),
                name="licence_licence_toggle_enabled",  # 使用下划线而不是破折号
            ),
        ]
        return custom_urls + urls

    def toggle_enabled(self, request, pk, *args, **kwargs):
        """根据当前enabled的值，切换为0或1"""
        licence = Licence.objects.get(pk=pk)
        licence.enabled = 0 if licence.enabled == 1 else 1
        licence.save()
        return redirect(reverse('admin:licence_licence_changelist')) # 返回到上一层列表页


# /admin/licence/licence/toggle_enabled/12/