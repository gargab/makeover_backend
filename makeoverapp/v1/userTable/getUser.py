from makeoverapp.models import *
from makeoverapp.serializers import *

def getUser(phone_no):

    user_recv= user.objects.get(phone_number=phone_no)
    return user_serializer(user_recv).data
