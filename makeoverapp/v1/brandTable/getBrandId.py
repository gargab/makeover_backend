from makeoverapp.models import *
from makeoverapp.serializers import *

def getBrandId(name):

    recv_brand_id = brand.objects.filter(name=name)[0].id
    return recv_brand_id
