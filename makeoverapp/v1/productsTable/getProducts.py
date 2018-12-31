from makeoverapp.models import *
from makeoverapp.serializers import *
from collections import defaultdict

from makeoverapp.v1.categoriesTable.getCategories import *
from makeoverapp.v1.brandTable.getBrands import *

def getProducts():

    brands = getBrands()
    return_obj=defaultdict()
    for brand in brands:
        categories = getCategories()
        category_dict = defaultdict()
        for category in categories:
            products = product.objects.filter(category_id = category.id, brand_id=brand.id).values_list('product_id', flat=True)
            if len(products) != 0:
                category_dict[category.name] = products
        if len(category_dict) != 0:
            return_obj[brand.name] = category_dict
    return return_obj
