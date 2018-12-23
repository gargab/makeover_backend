from makeoverapp.models import *
from makeoverapp.serializers import *

def getGroupId(phone_no):

    user_group= user.objects.get(phone_number=phone_no).group_id
    return user_group
