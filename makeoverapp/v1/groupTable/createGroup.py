from makeoverapp.models import *
from makeoverapp.serializers import *

def createGroup(phone_no, name):

    group_dict={}
    group_dict['name']=name
    group_dict['created_by']=phone_no

    group_dict_serial=group_serializer(data=group_dict)

    if group_dict_serial.is_valid():
        group_dict_serial.save()
        return True

    else:
        return False
