from makeoverapp.models import *
from makeoverapp.serializers import *

import random

def otp(phone_no):

    otp_got = random.randrange(100000, 1000000)
    if user.objects.filter(token=otp_got).exists():
        return otp(phone_no)
    else:
        u_user = user.objects.get(phone_number=phone_no)
        u_user.token=otp_got
        u_user.save()
        return otp_got
