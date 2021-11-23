from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from .models import ProductCategory, Product

admin.site.register(ProductCategory)
admin.site.register(Product)
# Register your models here.
