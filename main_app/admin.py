from django.contrib import admin
from . models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id','email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)





admin.site.register(CustomUser, CustomUserAdmin)
