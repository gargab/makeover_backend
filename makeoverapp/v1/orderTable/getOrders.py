from makeoverapp.models import *
from makeoverapp.serializers import *

from makeoverapp.v1.customerTable.getCustomerById import *
from makeoverapp.v1.userTable.getUser import *
from makeoverapp.v1.userTable.isAdmin import *


def getOrders(phone_no):

    orders_arr=[]

    if isAdmin(phone_no):
        orders=order.objects.all()
    else:
        orders= order.objects.filter(agent_id=phone_no)

    for order_obj in orders:
        order_dict={}
        order_dict=getCustomerById(order_obj.customer_id)
        order_dict['id'] = order_obj.id
        order_dict['status'] = order_obj.status
        user_info = getUser(phone_no)
        order_dict['agent_name'] = user_info['first_name'] + ' ' + user_info['last_name']
        order_dict['total']=order_obj.order_value
        order_dict['timestamp']=order_obj.timestamp.strftime('%b %-d %Y %-I:%-M %p')
        orders_arr.append(order_dict)

    return orders_arr
