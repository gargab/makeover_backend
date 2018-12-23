from makeoverapp.models import *
from makeoverapp.serializers import *

def getCategories():

    recv_categories = categories.objects.all()
    return recv_categories
