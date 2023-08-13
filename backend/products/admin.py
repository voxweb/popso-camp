from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ("store", "offer_id", "name",)

    list_display = ["store", "offer_id", "name",]

    list_display_links = (
        "store",
        "offer_id",
    )

    list_per_page = 30


admin.site.site_header = "Админ панель"
admin.site.site_title = "Управление данными"
admin.site.index_title = "APP"
