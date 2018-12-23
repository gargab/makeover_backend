from makeoverapp.models import *
from makeoverapp.serializers import *

from makeoverapp.v1.userTable.getUser import *

def getCustomers(phone_no):

    recv_group_id = getUser(phone_no)['group_id']
    customers_recv= customer.objects.filter(group_id=recv_group_id)
    return customer_serializer(customers_recv, many=True).data
