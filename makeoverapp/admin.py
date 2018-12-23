from django.contrib import admin
from models import *
# Register your models here.
##Register your models here to view them in the admin page
#admin.site.register(item)
admin.site.register(user)
admin.site.register(group)
admin.site.register(categories)
admin.site.register(brand)
admin.site.register(product)
admin.site.register(customer)
admin.site.register(order)
admin.site.register(order_products)
