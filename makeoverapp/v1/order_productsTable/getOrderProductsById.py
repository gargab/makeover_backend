from makeoverapp.models import *
from makeoverapp.serializers import *


def getOrderProductsById(order_id):

    order_products_obj= order_products.objects.filter(order_id=order_id)
    print order_products_obj
    return order_products_obj
