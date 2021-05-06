from django.contrib import admin
from .models import Banner , Product, Customer, Seller, Item, Review, Tag, Category, ShippingCosts

# Register your models here.

admin.site.register([Product, Banner,  Customer, Seller, Item, Review, Tag, Category, ShippingCosts])
