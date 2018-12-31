from makeoverapp.models import *
from makeoverapp.serializers import *


def createOrderProductsDict(product_table_id, quantity, order_id):
    order_product_dict={}
    order_product_dict['product_table_id']=product_table_id
    order_product_dict['quantity']=quantity
    order_product_dict['order_id']=order_id
    order_product_dict_serial = order_products_serializer(data=order_product_dict)
    if order_product_dict_serial.is_valid():
        return order_product_dict
    else:
        return {}
