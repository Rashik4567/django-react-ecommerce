from re import T
from django.shortcuts import render

from rest_framework import status
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import BannerSerializer, ReviewPostSerializer, ProductAddSerializer, ProductSerializer, ReviewSerializer,  TagsSerializer
from .models import Banner, Category, Customer, Item, Product, Review, Seller, ShippingCosts, Tag, Variations


@api_view(["GET"])
def productlist(request, end):
    products = Product.objects.all().order_by("-Release_date")[:(int(end))]
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def productcreate(request):
    if request.method == "POST":
        serializer = ProductAddSerializer(
            data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def productget(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


@api_view(["GET", "POST"])
def reviews(request):
    reviews = Review.objects.all()
    serializer = ProductSerializer(reviews, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def tags(request, pk):
    tags = Tag.objects.get(id=int(pk))
    serializer = TagsSerializer(tags, many=False)
    return Response(serializer.data)


@api_view(["GET", "POST"])
def variations(request, pk):
    product = Product.objects.get(id=pk)
    variations_of_product = Product.objects.filter(
        Product_Variation=product.Product_Variation).exclude(id=pk)
    serializer = ProductSerializer(variations_of_product, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def banner(request):
    banners = Banner.objects.all()
    serializer = BannerSerializer(banners, many=True)

    return Response(serializer.data)


@api_view(["POST"])
def review_post(request):
    if request.method == "POST":
        serializer = ReviewPostSerializer(
            data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def reviews_of_product(request, product_id):
    product = Product.objects.get(id=product_id)
    serializer = ReviewSerializer(product, many=True)

    return Response(serializer.data)
