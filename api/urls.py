from django.urls import path
from . import views

urlpatterns = [
    path('products/<int:end>', views.productlist),
    path('reviews', views.reviews),
    path('product/create', views.productcreate),
    path('product/get/<str:pk>', views.productget),
    path('tags/<int:pk>', views.tags),
    path('variations/<int:pk>', views.variations),
    path("banner", views.banner),
]
