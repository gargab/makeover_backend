from django.conf.urls import include,url
from django.conf import settings


urlpatterns = [
    url(r'^v1/',include('makeoverapp.v1.urls'))
]
