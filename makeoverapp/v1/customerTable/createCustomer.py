from makeoverapp.models import *
from makeoverapp.serializers import *

def createCustomer(local_customer):

    if customer.objects.filter(group_id=local_customer['group_id'], phone_number=local_customer['phone_number']).exists():
        return False
    else:
        customer_serial = customer_serializer(data=local_customer)
        if customer_serial.is_valid():
            customer_serial.save()
            return True
        else:
            print customer_serial.errors
            return False
