from makeoverapp.models import *
from makeoverapp.serializers import *
from collections import defaultdict

from makeoverapp.v1.categoriesTable.getCategories import *
from makeoverapp.v1.brandTable.getBrands import *

def getProductTableId(shade, brand_id, category_id):

    product_table_id = product.objects.filter(product_id=shade, category_id=category_id, brand_id=brand_id)[0].id
    return product_table_id
