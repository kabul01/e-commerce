from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Product, Category



class CategoryAdmiin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','slug','price','category','available','created']
    list_filter = ['available','created']
    list_editable = ['price','available']
    prepopulated_fields = {'slug':('name',)}







admin.site.register(Category,CategoryAdmiin)
admin.site.register(Product,ProductAdmin)