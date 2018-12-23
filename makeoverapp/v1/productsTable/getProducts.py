from makeoverapp.models import *
from makeoverapp.serializers import *
from collections import defaultdict

from makeoverapp.v1.categoriesTable.getCategories import *
from makeoverapp.v1.brandTable.getBrands import *

def getProducts():

    categories = getCategories()
    return_obj = defaultdict()
    for category in categories:
        brands = getBrands()
        brand_dict=defaultdict(list)
        for brand in brands:
            products = product.objects.filter(category_id = category.id, brand_id=brand.id).values_list('product_id', flat=True)
            if len(products) != 0:
                brand_dict[brand.name] = products
        return_obj[category.name] = brand_dict
    return return_obj
