from celery import shared_task
from celery_singleton import Singleton
from requests import RequestException
from urllib3.exceptions import NewConnectionError


@shared_task(
    base=Singleton,
    name="update_create_products",
    auto_retry=[RequestException, NewConnectionError],
    max_retries=2,
    queue="products",
)
def update_create_products():
    return True    # here you can add your method to update/create products