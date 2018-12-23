from rest_framework import serializers
from models import *

class user_serializer(serializers.ModelSerializer):
	class Meta:
		model=user
		fields='__all__'#optional, name of fields to return as a list

class group_serializer(serializers.ModelSerializer):
	class Meta:
		model=group
		fields='__all__'#optional, name of fields to return as a list

class categories_serializer(serializers.ModelSerializer):
	class Meta:
		model=categories
		fields='__all__'#optional, name of fields to return as a list

class brand_serializer(serializers.ModelSerializer):
	class Meta:
		model=brand
		fields='__all__'#optional, name of fields to return as a list

class product_serializer(serializers.ModelSerializer):
	class Meta:
		model=product
		fields='__all__'#optional, name of fields to return as a list

class customer_serializer(serializers.ModelSerializer):
	class Meta:
		model=customer
		fields='__all__'#optional, name of fields to return as a list

class order_serializer(serializers.ModelSerializer):
	class Meta:
		model=order
		fields='__all__'#optional, name of fields to return as a list

class order_products_serializer(serializers.ModelSerializer):
	class Meta:
		model=order_products
		fields='__all__'#optional, name of fields to return as a list
