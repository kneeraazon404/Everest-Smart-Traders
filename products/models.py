# Create your models here.
from django.db import models
from django.urls import reverse  # For generating URLs by reversing URL patterns


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"pk": self.pk})

    class Meta:
        verbose_name_plural = "Categories"


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


from django.db import models
from django.urls import reverse


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="products/%Y/%m/%d/", blank=True)
    categories = models.ManyToManyField(
        "Category", related_name="products"
    )  # Assuming you have a Category model defined elsewhere
    tags = models.ManyToManyField(
        "Tag", related_name="products"
    )  # Assuming you have a Tag model defined elsewhere
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"pk": self.pk})


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, related_name="images", on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="product_images/%Y/%m/%d/")

    def __str__(self):
        return f"{self.product.name} Image"


class ContactPage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="contacts/%Y/%m/%d/", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Contact page"
        verbose_name_plural = "Contact page"

    def get_absolute_url(self):
        return reverse("contact_detail", kwargs={"pk": self.pk})


class HomePage(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Home page"
        verbose_name_plural = "Home page"

    def get_absolute_url(self):
        return reverse("home_detail", kwargs={"pk": self.pk})


class AboutPage(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "About page"
        verbose_name_plural = "About page"

    def get_absolute_url(self):
        return reverse("about_detail", kwargs={"pk": self.pk})
