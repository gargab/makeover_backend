from makeoverapp.models import *
from makeoverapp.serializers import *

from makeoverapp.v1.brandTable.getBrandId import *
from makeoverapp.v1.categoriesTable.getCategoryId import *
from makeoverapp.v1.productsTable.getProductTableId import *
from makeoverapp.v1.order_productsTable.createOrderProductsDict import *
from makeoverapp.v1.order_productsTable.saveOrderProducts import *
from makeoverapp.v1.userTable.getGroupId import *

def createOrder(agent_id, product_json):
    print(product_json)

    OrderProducts=[]
    order_dict={}
    order_dict['agent_id']=agent_id
    order_dict['customer_id']=product_json['customer_id']
    order_dict['status']='Pending'
    order_dict['group_id']=getGroupId(str(agent_id))

    try:
        latest_id=order.objects.latest('id').id
    except:
        latest_id = -1

    order_map=product_json['orderMap']

    order_dict ['order_value']= sum(order_map.values())

    for key in order_map:
        BCS = key.split('_')
        brand = BCS[0]
        category = BCS[1]
        shade = BCS[2]
        brand_id = getBrandId(brand)
        category_id = getCategoryId(category)
        product_table_id= getProductTableId(shade, brand_id, category_id)
        ret_dict = createOrderProductsDict(product_table_id, order_map[key], latest_id+1)
        if len(ret_dict) == 0:
            return False
        else:
            OrderProducts.append(ret_dict)
    print OrderProducts
    if saveOrderProducts(OrderProducts):
        order_serial = order_serializer(data=order_dict)
        if order_serial.is_valid():
            order_serial.save()
            return True
        else:
            print "Here"
            print order_serial.errors
            return False
    else:
        return False
