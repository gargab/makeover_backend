from makeoverapp.models import *
from makeoverapp.serializers import *

def getCategoryId(name):

    recv_category_id = categories.objects.filter(name=name)[0].id
    return recv_category_id
