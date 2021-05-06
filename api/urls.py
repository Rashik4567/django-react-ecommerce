from django.urls import path
from . import views

urlpatterns = [
    path('products/<int:end>', views.productlist),
    path('reviews', views.reviews),
    path('shipping/costs/get/<str:country>/<str:sellerid>', views.shipping_cost_get),
    path('shipping/costs/add', views.shipping_cost_add),
    path('items', views.items),
    path('customer/data/<str:pk>', views.customerget),
    path('customer/create', views.customercreate),
    path('seller/get/<str:pk>', views.sellerget),
    path('seller/create', views.sellercreate),
    path('product/create', views.productcreate),
    path('product/get/<str:pk>', views.productget),
    path('tags/<int:pk>', views.tags),
    path('categories', views.categories),
    path('category/<str:pk>', views.categoryget),
    path('variations', views.variations),
    path("banner", views.banner),
]
