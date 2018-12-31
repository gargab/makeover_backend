from makeoverapp.models import *
from makeoverapp.serializers import *


def getCategoryById(category_id):

    category_obj = categories.objects.get(id=category_id)
    return category_obj
