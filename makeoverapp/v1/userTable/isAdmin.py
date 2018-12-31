from makeoverapp.models import *
from makeoverapp.serializers import *

def isAdmin(phone_no):

    user_recv= user.objects.get(phone_number=phone_no)
    if user_recv.admin == 1:
        return True
    else:
        return False
