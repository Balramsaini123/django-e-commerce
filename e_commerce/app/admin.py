from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(slider)
admin.site.register(banner_area)
admin.site.register(Main_Category)
admin.site.register(Category)
admin.site.register(Sub_Category)
admin.site.register(Section)


class Product_images(admin.TabularInline):
    model = Product_image


class Additional_informations(admin.TabularInline):
    model = Additional_information


class Product_Admin(admin.ModelAdmin):
    inlines = (Product_images, Additional_informations)


admin.site.register(Product, Product_Admin)
admin.site.register(Product_image)
admin.site.register(Additional_information)





