from django.contrib import admin
from . models import Goods_Fabric, Payment
from django.contrib.auth.models import Group, User

admin.site.register(Goods_Fabric)
admin.site.register(Payment)

admin.site.unregister(Group)
admin.site.unregister(User)