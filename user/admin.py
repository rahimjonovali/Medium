from django.contrib import admin

from .models import *


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id','username', 'email', 'first_name', 'last_name')
    search_fields = ('username', 'first_name', 'last_name')
    list_filter = ('email', 'first_name', 'last_name')
    list_display_links = ('username', 'email', 'first_name', 'last_name')

admin.site.register(CustomUser, CustomUserAdmin)
