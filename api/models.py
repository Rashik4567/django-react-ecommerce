from django.db import models

from django.contrib.auth.models import User
from django_countries.fields import CountryField


# For more details for database design and progress, please visit the link below
# https://drawsql.app/ai-explorers/diagrams/r-shop-premium


RatingChoices = [
    (1, "1"),
    (2, "2"),
    (3, "3"),
    (4, "4"),
    (5, "5"),
]


class Customer(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Country = CountryField(blank_label="Select your country")
    Picture = models.ImageField(
        upload_to="CustomerProfiles/",
        null=True,
        blank=True)
    Creation_date = models.DateTimeField(auto_now_add=True)
    Primary_shipping_address = models.CharField(
        max_length=355, null=True, blank=True)

    def __str__(self):
        return (self.User.username)


class Seller(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Country = CountryField(blank_label="Select your country")
    Picture = models.ImageField(
        upload_to="SellerProfiles/",
        null=True,
        blank=True)
    Varified = models.BooleanField(default=False, editable=False)
    Creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (self.User.username)


class ShippingCosts(models.Model):
    Country_Region = CountryField(blank_label="Select your country")
    Cost = models.PositiveIntegerField()
    Seller = models.ForeignKey(Seller, on_delete=models.CASCADE)

    def __str__(self):
        return (self.Seller.User.username)


class Category(models.Model):
    Category_name = models.CharField(max_length=355)
    Category_Picture = models.ImageField(upload_to="CategoryImages/")
    Category_description = models.CharField(max_length=3_555)

    def __str__(self):
        return self.Category_name

    class Meta:
        verbose_name_plural = "Categories"


class Tag(models.Model):
    Name = models.CharField(max_length=355)
    Color_HEX = models.CharField(max_length=10)

    def __str__(self):
        return self.Name


class Variations(models.Model):
    Common_title = models.CharField(max_length=355)

    def __str__(self):
        return self.Common_title


class Product(models.Model):
    Title = models.CharField(max_length=355)
    Description = models.CharField(max_length=3_555)
    Price = models.FloatField()
    Seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    Release_date = models.DateTimeField(auto_now_add=True)
    Made_in = CountryField(
        blank_label="Select your country", null=True, blank=True)
    Main_picture = models.ImageField(upload_to="ProductPhotos/")
    Second_picture = models.ImageField(
        upload_to="ProductPhotos/", null=True, blank=True)
    Third_picture = models.ImageField(
        upload_to="ProductPhotos/", null=True, blank=True)
    Forth_picture = models.ImageField(
        upload_to="ProductPhotos/", null=True, blank=True)
    Fifth_picture = models.ImageField(
        upload_to="ProductPhotos/", null=True, blank=True)
    First_video = models.FileField(
        upload_to="ProductVideos/", null=True, blank=True)
    Second_video = models.FileField(
        upload_to="ProductVideos/", null=True, blank=True)
    Stock = models.IntegerField()
    Product_Variation = models.ForeignKey(
        Variations, on_delete=models.SET_NULL, null=True, blank=True)
    Expire_date = models.DateField(null=True, blank=True)
    Category_Of_Product = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True)
    Tag1 = models.ForeignKey(
        Tag,
        related_name="Tag1",
        on_delete=models.SET_NULL,
        null=True,
        blank=True)
    Tag2 = models.ForeignKey(
        Tag,
        related_name="Tag2",
        on_delete=models.SET_NULL,
        null=True,
        blank=True)
    Tag3 = models.ForeignKey(
        Tag,
        related_name="Tag3",
        on_delete=models.SET_NULL,
        null=True,
        blank=True)

    def __str__(self):
        return self.Title

    class Meta:
        get_latest_by = "Release_date"


class Review(models.Model):
    By = models.ForeignKey(Customer, on_delete=models.CASCADE)
    To = models.ForeignKey(Product, on_delete=models.CASCADE)
    Rating = models.IntegerField(choices=RatingChoices)
    Comment = models.CharField(max_length=3_555, null=True, blank=True)

    def __str__(self):
        return self.Rating


class Item(models.Model):
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    Author = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Ammount = models.IntegerField(default=1)

    def __str__(self):
        return self.Product.Title


class Banner(models.Model):
    Creation_date = models.DateTimeField(auto_now_add=True)
    Name = models.CharField(max_length=255)
    Image = models.ImageField(upload_to="bannerimages/")
    On_click_url = models.CharField(max_length=3_555)

    def __str__(self):
        return self.Name

    class Meta:
        get_latest_by = "Creation_date"
