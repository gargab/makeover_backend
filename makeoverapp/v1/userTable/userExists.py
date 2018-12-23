from makeoverapp.models import *
from makeoverapp.serializers import *

def userExists(phone_no):
    if user.objects.filter(phone_number=phone_no).exists():
        return True
    else:
        return False
