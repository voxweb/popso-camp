from rest_framework.mixins import CreateModelMixin, ListModelMixin
from drf_yasg.utils import swagger_auto_schema
from rest_framework.viewsets import GenericViewSet
from products.models import Product
from products.tasks import update_create_products
from products.serializers import ProductSerializer

# Create your views here.

class ProductApi(CreateModelMixin, ListModelMixin, GenericViewSet):
    serializer_class = ProductSerializer

    @swagger_auto_schema(
        tags=["Товары"],
        operation_id="Получение каталога товаров",
        operation_description="GET запрос на получение каталога товаров.",
    )

    def get_queryset(self):
        return (
            Product.objects.filter(store__user_id=self.request.user.pk)
        )

    @swagger_auto_schema(
        tags=["Товары"],
        operation_id="Получение каталога товаров",
        operation_description="POST запрос запускает задачу на получение каталога товаров маркетплейса.",
    )
    def create(self, request, *args, **kwargs):
        update_create_products.delay()
