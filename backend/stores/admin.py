from django.contrib import admin
from stores.models import Store
from products.models import Product


class StoreProducts(admin.StackedInline):
    model = Product
    verbose_name_plural = "Товары магазина"
    fields = ("offer_id",)
    max_num = 5
    extra = 0
    classes = ["collapse", "show"]


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "user",
        "name",
    )

    list_display_links = (
        "user",
        "name",
    )

    inlines = [
        StoreProducts,
    ]

admin.autodiscover()