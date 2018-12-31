from makeoverapp.models import *
from makeoverapp.serializers import *


def saveOrderProducts(orderProdArray):
    order_product_dict_serial = order_products_serializer(data=orderProdArray, many=True)
    if order_product_dict_serial.is_valid():
        order_product_dict_serial.save()
        return True
    else:
        print order_product_dict_serial.errors
        return False
