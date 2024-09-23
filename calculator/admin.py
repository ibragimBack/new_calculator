from typing import Any
from django.contrib import admin
from django.http import HttpRequest
from . models import Goods_Fabric, Payment, Icon, Discount
from django.contrib.auth.models import Group, User
from django.contrib.admin import AdminSite

class IconAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if Icon.objects.exists():
            return False
        return super().has_add_permission(request)
    
class DiscountAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if Discount.objects.exists():
            return False
        return super().has_add_permission(request)

admin.site.register(Goods_Fabric)
admin.site.register(Payment)
admin.site.register(Icon, IconAdmin)
admin.site.register(Discount, DiscountAdmin)

admin.site.unregister(Group)
admin.site.unregister(User)