from django.contrib import admin
from app.models import Products,Categories


class AdminProducts(admin.ModelAdmin):
    list_display=['name','price','category','image','description']

class AdminCategories(admin.ModelAdmin):
    list_display=['name','image']


# Register your models here.

admin.site.register(Products,AdminProducts)
admin.site.register(Categories,AdminCategories)