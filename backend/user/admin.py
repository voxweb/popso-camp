from django.contrib import admin
from user.models import User
from stores.models import Store


class StoreInline(admin.StackedInline):
    model = Store


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = [
        StoreInline,
    ]

    list_display = (
        "username",
        "phone",
    )

admin.autodiscover()