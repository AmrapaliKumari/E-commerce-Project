from encodings import search_function
from unicodedata import category
from django.contrib import admin

from .models import Products, Orders
from django.contrib import admin
# Register your models here.

admin.site.site_header="E-commerce site"
admin.site.site_title="ABC shopping "
admin.site.index_title="Manage ABC shopping"

class productsAdmin(admin.ModelAdmin):

    def change_category_to_default(self,request,queryset):
        queryset.update(category="default")


    change_category_to_default.short_description='Default Category'

    list_display=('title','price','category','description','image')
    search_fields=('title',)
    actions=('change_category_to_default',)
    fields=('title','price',)
    list_editable=('price','category',)

admin.site.register(Products,productsAdmin)
admin.site.register(Orders)


