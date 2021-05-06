from django.contrib import admin
from .models import Banner , Product, Customer, Seller, Item, Review, Tag, Category, ShippingCosts, Variations

# Register your models here.

admin.site.register([Product, Banner, Variations, Customer, Seller, Item, Review, Tag, Category, ShippingCosts])
