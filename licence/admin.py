from django.contrib import admin
from django.urls import path, reverse
from django.shortcuts import redirect
from django.utils.html import format_html
import uuid
from .models import Licence
# Register your models here.
@admin.register(Licence)
class LicenceAdmin(admin.ModelAdmin):
    list_display = ("machine_code","type","remark","status","type_button")
    
    def type_button(self, obj):
        """在列表里显示按钮：若启用则显示“禁用”，若停用则显示“启用”"""
        if obj.enabled == 1:
            return format_html(
                '<a class="el-button stop-submit el-button--danger el-button--small" style="color:white" href="{}">禁用</a>',
                reverse("admin:licence-licence-toggle-enabled", args=[obj.pk])
            )
        else:
            return format_html(
                '<a class="el-button el-button--primary el-button--small" style="color:white" href="{}">启用</a>',
                reverse("admin:licence-licence-toggle-enabled", args=[obj.pk])
            )
    type_button.short_description = "操作"

    def get_urls(self):
        """定义自定义URL，用于切换enabled值"""
        urls = super().get_urls()
        custom_urls = [
            path(
                "toggle_enabled/<int:pk>/",
                self.admin_site.admin_view(self.toggle_enabled),
                name="licence-licence-toggle-enabled",
            ),
        ]
        return custom_urls + urls

    def toggle_enabled(self, request, pk, *args, **kwargs):
        """根据当前enabled的值，切换为0或1"""
        licence = Licence.objects.get(pk=pk)
        licence.enabled = 0 if licence.enabled == 1 else 1
        licence.save()
        return redirect("../")  # 返回到上一层列表页
