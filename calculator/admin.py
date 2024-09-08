from typing import Any
from django.contrib import admin
from . models import Goods_Fabric, Payment, Discount, Icon
from django.contrib.auth.models import Group, User
from django.contrib.admin import AdminSite

class IconAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if Icon.objects.exists():
            return False
        return super().has_add_permission(request)

admin.site.register(Goods_Fabric)
admin.site.register(Payment)
admin.site.register(Icon, IconAdmin)
@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ('min_price', 'max_price', 'discount_percentage')

admin.site.unregister(Group)
admin.site.unregister(User)