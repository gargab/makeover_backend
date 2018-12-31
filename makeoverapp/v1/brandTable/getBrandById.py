from makeoverapp.models import *
from makeoverapp.serializers import *


def getBrandById(brand_id):

    brand_obj = brand.objects.get(id=brand_id)
    return brand_obj
