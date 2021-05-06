from django.db.models import fields
from .models import   Banner, Category, Customer, Item, Product, Review, Seller, ShippingCosts, Tag, Variations
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ProductAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["Title", "Description", "Release_date", "Made_in", "Main_picture", "Second_picture", "Second_picture", "Forth_picture",
                  "Fifth_picture", "First_video", "Second_video", "Stock", "Expire_date", "Category_Of_Product", "Tag1", "Tag2", "Tag3"]

    def save(self, **kwargs):
        User = self.context["request"].user
        Seller = Seller.objects.get(User=User)
        validated_data = dict(
            list(self.validated_data.items()) +
            list(kwargs.items())
        )
        validated_data["Seller"] = Seller
        self.instance = self.create(validated_data)
        return self.instance


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ["Country", "Picture",
                  "Creation_date", "Primary_shipping_address"]

    def save(self, **kwargs):
        User = self.context['request'].user
        validated_data = dict(
            list(self.validated_data.items()) +
            list(kwargs.items())
        )
        validated_data["User"] = User
        self.instance = self.create(validated_data)
        return self.instance


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = ["Country", "Picture", "Creation_date", "Varified"]

    def save(self, **kwargs):
        User = self.context['request'].user
        validated_data = dict(
            list(self.validated_data.items()) +
            list(kwargs.items())
        )
        validated_data["User"] = User
        self.instance = self.create(validated_data)
        return self.instance


class ShippingCostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingCosts
        fields = ["Country_Region", "Cost"]

    def save(self, **kwargs):
        User = self.context['request'].user
        Seller0 = Seller.objects.filter(User=User)[0]
        validated_data = dict(
            list(self.validated_data.items()) +
            list(kwargs.items())
        )
        validated_data["Seller"] = Seller0
        self.instance = self.create(validated_data)
        return self.instance


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class VariationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variations
        fields = "__all__"


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = "__all__"

