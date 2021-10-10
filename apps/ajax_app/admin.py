from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    ordering = ("created_at",)
    list_filter = ('id', 'name', 'user',)
    list_display = ('id', 'user', 'name', 'description', 'quantity', 'image', 'created_at', 'updated_at',)
    search_fields = ('id', 'name', 'user',)