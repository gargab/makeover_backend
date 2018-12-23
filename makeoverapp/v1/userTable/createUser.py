from makeoverapp.models import *
from makeoverapp.serializers import *

def createUser(user):

    user_serial = user_serializer(data=user)
    if user_serial.is_valid():
        user_serial.save()
        return True
    else:
        print user_serial.errors
        return False
