from django.contrib import admin
from .models import (
    Category,
    Tag,
    Product,
    ContactPage,
    HomePage,
    AboutPage,
    ProductImage,
)

# Register your models here.


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(ContactPage)
admin.site.register(HomePage)
admin.site.register(AboutPage)


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductImageInline,
    ]
    list_display = (
        "name",
        "created_at",
        "updated_at",
    )
    list_filter = (
        "created_at",
        "updated_at",
    )
    search_fields = ("name",)


admin.site.register(Product, ProductAdmin)
