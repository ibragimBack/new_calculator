from typing import Any
from django.contrib import admin
from . models import Payment, Icon
from django.contrib.auth.models import Group, User

class IconAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if Icon.objects.exists():
            return False
        return super().has_add_permission(request)

admin.site.register(Payment)
admin.site.register(Icon, IconAdmin)

admin.site.unregister(Group)
admin.site.unregister(User)