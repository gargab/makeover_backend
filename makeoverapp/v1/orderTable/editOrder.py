from makeoverapp.models import *
from makeoverapp.serializers import *

from makeoverapp.v1.brandTable.getBrandId import *
from makeoverapp.v1.categoriesTable.getCategoryId import *
from makeoverapp.v1.productsTable.getProductTableId import *
from makeoverapp.v1.order_productsTable.createOrderProductsDict import *
from makeoverapp.v1.order_productsTable.saveOrderProducts import *
from makeoverapp.v1.userTable.getGroupId import *

def editOrder(phone_no, order_json):


    order_id=order_json['order_id']
    order_map=order_json['orderMap']

    order_obj = order.objects.get(id=order_id)

    if order_obj.agent_id != phone_no and isAdmin(phone_no) == 0:
        return False

    ids_changed = []
    for key in order_map:
        BCS = key.split('_')
        brand = BCS[0]
        category = BCS[1]
        shade = BCS[2]
        brand_id = getBrandId(brand)
        category_id = getCategoryId(category)
        product_table_id = getProductTableId(shade, brand_id, category_id)

        try:
            orderProductItem = order_products.objects.get(order_id=order_id, product_table_id=product_table_id)
            print orderProductItem.quantity
            print order_map[key]
            orderProductItem.quantity = order_map[key]
            orderProductItem.save()
            ids_changed.append(orderProductItem.id)

        except:
            orderProductDict={}
            orderProductDict['product_table_id']=product_table_id
            orderProductDict['order_id'] = order_id
            orderProductDict['quantity'] = order_map[key]
            orderProductserial = order_products_serializer(data=orderProductDict)
            if orderProductserial.is_valid():
                orderProductserial.save()
            else:
                return False

    all_order_product_ids = order_products.objects.filter(order_id=order_id).values_list('id', flat=True)

    for id in all_order_product_ids:
        if id not in ids_changed:
            order_products.objects.get(id=id).delete()

    return True
