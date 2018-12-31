from makeoverapp.models import *
from makeoverapp.serializers import *

from makeoverapp.v1.productsTable.getProductById import *
from makeoverapp.v1.brandTable.getBrandById import *
from makeoverapp.v1.categoriesTable.getCategoryById import *
from makeoverapp.v1.order_productsTable.getOrderProductsById import *
from makeoverapp.v1.userTable.isAdmin import *


def getDetailedOrderById(phone_no, order_id):

    order_dict={}
    order_obj=order.objects.get(id=order_id)

    if order_obj.agent_id != phone_no and isAdmin(phone_no) == 0:
        return {}

    else:
        ordered_products = getOrderProductsById(order_id)
        order_dict={}
        for order_product in ordered_products:
            product_obj = getProductById(order_product.product_table_id)
            brand_name = getBrandById(product_obj.brand_id).name
            category_name = getCategoryById(product_obj.category_id).name
            shade_name = product_obj.product_id
            key = brand_name + '_' + category_name + '_' + shade_name
            order_dict[key] = order_product.quantity

        compiled_order_dict={}
        compiled_order_dict['order_id'] = order_id
        compiled_order_dict['orderMap'] = order_dict

    return compiled_order_dict
