from makeoverapp.models import *
from makeoverapp.serializers import *

from makeoverapp.v1.userTable.getUser import *

def getGroups():

    groups_recv=group.objects.all()
    group_serial = group_serializer(groups_recv, many=True)
    return group_serial.data
