from makeoverapp.models import *
from makeoverapp.serializers import *

def verify_otp(phone_no, otp):
    if user.objects.filter(phone_number=phone_no).exists():
        user_obj = user.objects.get(phone_number=phone_no)
        if user_obj.token == otp and user_obj.active == 1:
            return True
        else:
            return False
    else:
        return False
