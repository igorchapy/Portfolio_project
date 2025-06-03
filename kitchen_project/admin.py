from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Cook


class CookAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age', 'experience')}),
    )

admin.site.register(Cook, CookAdmin)
