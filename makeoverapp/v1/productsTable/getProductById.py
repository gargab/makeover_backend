from makeoverapp.models import *
from makeoverapp.serializers import *


def getProductById(product_id):

    product_obj = product.objects.get(id=product_id)
    return product_obj
