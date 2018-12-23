from makeoverapp.models import *
from makeoverapp.serializers import *

def getBrands():

    recv_brands = brand.objects.all()
    return recv_brands
