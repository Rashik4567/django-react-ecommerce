from django.db.models import fields
from .models import Banner, Customer, Product, Review, Tag, Seller
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
        seller = Seller.objects.get(User=User)
        validated_data = dict(
            list(self.validated_data.items()) +
            list(kwargs.items())
        )
        validated_data["Seller"] = seller
        self.instance = self.create(validated_data)
        return self.instance


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = "__all__"


class ReviewPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["To", "Rating", "Comment"]

    def save(self, **kwargs):
        User = self.context["request"].user
        By = Customer.objects.get(User=User)
        validated_data = dict(
            list(self.validated_data.items()) +
            list(kwargs.items())
        )
        validated_data["By"] = By
        self.instance = self.create(validated_data)
        return self.instance


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
