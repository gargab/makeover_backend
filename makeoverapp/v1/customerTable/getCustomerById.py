from makeoverapp.models import *
from makeoverapp.serializers import *


def getCustomerById(customer_id):

    customer_obj= customer.objects.filter(id=customer_id)[0]
    customer_dict={}
    customer_dict['customer_name']=customer_obj.name
    customer_dict['address']=customer_obj.address

    return customer_dict
