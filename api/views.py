from re import T
from django.shortcuts import render

from rest_framework import status
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import BannerSerializer,  CategorySerializer, ProductAddSerializer, CustomerSerializer, ItemSerializer, ProductSerializer, SellerSerializer, ShippingCostSerializer,  TagsSerializer, VariationSerializer
from .models import   Banner, Category, Customer, Item, Product, Review, Seller, ShippingCosts, Tag, Variations


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
def categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def categoryget(request, pk):
    category = Category.objects.get(id=pk)
    serializer = CategorySerializer(category, many=False)
    return Response(serializer.data)


@api_view(["GET"])
def customerget(request, pk):
    customer = Customer.objects.get(id=pk)
    serializer = CustomerSerializer(customer, many=False)
    return Response(serializer.data)


@api_view(["POST"])
def customercreate(request):
    serializer = CustomerSerializer(
        data=request.data, context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def sellerget(request, pk):
    seller = Seller.objects.all(id=pk)
    serializer = SellerSerializer(seller, many=False)
    return Response(serializer.data)


@api_view(["POST"])
def sellercreate(request):
    if request.method == "POST":
        serializer = SellerSerializer(
            data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def shipping_cost_get(request, country, sellerid):
    fields = ShippingCosts.objects.get(
        Country_Region=country, Seller=Seller.objects.get(id=sellerid))
    serializer = ShippingCostSerializer(fields, many=False)
    return Response(serializer.data)


@api_view(["POST"])
def shipping_cost_add(request):
    if request.method == "POST":
        serializer = ShippingCostSerializer(
            data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def tags(request, pk):
    tags = Tag.objects.get(id=int(pk))
    serializer = TagsSerializer(tags, many=False)
    return Response(serializer.data)


@api_view(["GET", "POST"])
def variations(request):
    variations = Variations.objects.all()
    serializer = VariationSerializer(variations, many=True)
    return Response(serializer.data)


@api_view(["GET", "POST"])
def items(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def banner(request):
    banners = Banner.objects.all()
    serializer = BannerSerializer(banners, many=True)

    return Response(serializer.data)

