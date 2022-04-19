from django.contrib import admin
from . models import Property, Type, Message

# Register your models here.

@admin.register(Property)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "location","host","price")
    search_fields = ("name__startswith", "type__startswith" )
    list_filter = ("name", "type", "price","location" )

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    pass

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("user", "body")
    search_fields = ("user__startswith", "body__startswith" )
    list_filter = ("user", "property")