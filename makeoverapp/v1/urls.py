from django.conf.urls import include,url
from django.conf import settings
from . import views

urlpatterns = [
    url(r'^(?P<pk_1>.*)/user/(?P<pk_2>.*)', views.user.as_view(),name='userTableClass'),
    url(r'^login', views.login.as_view(), name='loginClass'),
    url(r'^(?P<pk_1>.*)/customer', views.customer.as_view(), name='customerClass'),
    url(r'^(?P<pk_1>.*)/product', views.product.as_view(), name='productClass')
    #url(r'^plant/(?P<pk>[0-9]+)/',views.plant.as_view(),name='plantTableClass'),
    #url(r'^equipment/(?P<pk>[0-9]+)/',views.equipment.as_view(),name='equipmentTableClass'),
]
