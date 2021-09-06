from django.contrib import admin
from .models import bought_items
# from django_tenants.admin import TenantAdminMixin

# from .models import Entity

# @admin.register(Entity)
# class ClientAdmin(TenantAdminMixin, admin.ModelAdmin):
#         list_display = ('name', 'on_trial','created_on')
admin.site.register(bought_items)