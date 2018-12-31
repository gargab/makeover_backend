from django.shortcuts import render
from makeoverapp.models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from makeoverapp.serializers import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import detail_route, list_route
from rest_framework import permissions, routers, serializers, viewsets
from django.http import HttpResponse
from datetime import date as dt
from datetime import timedelta,datetime,tzinfo
import json

from makeoverapp.v1.userTable.createUser import *
from makeoverapp.v1.userTable.userExists import *
from makeoverapp.v1.userTable.getUser import *
from makeoverapp.v1.userTable.getGroupId import *
from makeoverapp.v1.customerTable.getCustomers import *
from makeoverapp.v1.customerTable.createCustomer import *
from makeoverapp.v1.productsTable.getProducts import *
from makeoverapp.v1.orderTable.createOrder import *
from makeoverapp.v1.orderTable.getOrders import *
from makeoverapp.v1.orderTable.getDetailedOrderById import *
from makeoverapp.v1.orderTable.editOrder import *
from makeoverapp.v1.groupTable.getGroups import *
from makeoverapp.v1.groupTable.createGroup import *
from makeoverapp.v1.OTP.otp import *
from makeoverapp.v1.OTP.verify_otp import *
from makeoverapp.v1.SMS.send_sms import *
from makeoverapp.v1.stats.getStats import *

class user(APIView):

	def post(self,request,pk_1 = None,pk_2 = None):
		recv_json  = request.data
		otp_recv = recv_json['token']
		recv_json['data'] = user_json
		user_json['phone_number']=str(pk_2)
		user_json['created_by'] = str(pk_1)
		if verify_otp(str(pk_1), otp_recv):
			if createUser(user_json):
				return Response ({'data' : 'User Added'})

			else:
				return Response ({'data' : 'User Already Exists'})
		else:
			return Response({'data' : 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)


class login(APIView):

	def post(self, request):
		phone_no = str(request.data['phone_number'])
		if userExists(phone_no):
			otp_ret = otp(phone_no)
			#print send_sms('kXuAcv+ijWM-ucquAMD0BvmRIQ8AiV4mabWvXzWcUC', '91'+phone_no,'Makeover', 'The OTP to login to Makeover is ' + str(otp_ret))
			return Response ({'data' : 'SMS sent'})
		else:
			return Response({'data' : 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)

	def get(self, request):
		phone_no = request.GET.get('phone_number','0')
		otp_recv = request.GET.get('token','0')
		if verify_otp(phone_no, otp_recv):
			user_info = getUser(phone_no)
			for key in user_info.keys():
				user_info[key] = str(user_info[key])
			return Response (user_info)
		else:
			return Response({'data' : 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)

class customer(APIView):

	def post(self,request,pk_1 = None):
		customer_json  = request.data
		otp_recv = customer_json['token']
		if verify_otp(str(pk_1), otp_recv):
			customer_json['creator_id']=str(pk_1)
			customer_json['group_id'] = getGroupId(str(pk_1))
			if createCustomer(customer_json):
				return Response ({'data' : 'Customer Added'})

			else:
				return Response ({'data' : 'Customer with this Phone no. already exists'}, status=status.HTTP_400_BAD_REQUEST)
		else:
			return Response({'data' : 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)

	def get(self, request,pk_1 = None):
		phone_no = str(pk_1)
		otp_recv = request.GET.get('token','0')
		if verify_otp(phone_no, otp_recv):
			return Response (getCustomers(phone_no))
		else:
			return Response({'data' : 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)


class product(APIView):

	def get(self, request, pk_1=None):
		phone_no = str(pk_1)
		otp_recv = request.GET.get('token','0')
		if verify_otp(phone_no, otp_recv):
			return Response (getProducts())
		else:
			return Response({'data' : 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)

class orders(APIView):

	def post(self,request,pk_1 = None):
		product_json  = request.data
		otp_recv = product_json['token']
		if verify_otp(str(pk_1), otp_recv):
			if createOrder(pk_1, product_json):
				return Response({'data': 'Order Saved'})
			else:
				return Response ({'data' : 'Order Data error'}, status=status.HTTP_400_BAD_REQUEST)
		else:
			return Response({'data' : 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)

	def get(self,request,pk_1 = None):
		phone_no = str(pk_1)
		otp_recv = request.GET.get('token','0')
		if verify_otp(phone_no, otp_recv):
			return Response (getOrders(phone_no))
		else:
			return Response({'data' : 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)

class order(APIView):

	def get(self,request,pk_1=None, pk_2=None):
		phone_no = str(pk_1)
		otp_recv = request.GET.get('token','0')
		if verify_otp(phone_no, otp_recv):
			return Response (getDetailedOrderById(str(pk_1), str(pk_2)))
		else:
			return Response({'data' : 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)

	def post(self,request,pk_1 = None, pk_2=None):
		order_json  = request.data
		print (order_json)
		otp_recv = order_json['token']
		order_json['order_id'] = pk_2
		if verify_otp(str(pk_1), otp_recv):
			if editOrder(pk_1, order_json):
				return Response({'data': 'Order Edited'})
			else:
				return Response ({'data' : 'Order Data error'}, status=status.HTTP_400_BAD_REQUEST)
		else:
			return Response({'data' : 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)

class group(APIView):

	def get(self,request,pk_1=None):
		phone_no = str(pk_1)
		otp_recv = request.GET.get('token','0')
		if verify_otp(phone_no, otp_recv):
			return Response (getGroups())
		else:
			return Response({'data' : 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)

	def post(self,request,pk_1=None):
		group_json  = request.data
		otp_recv = group_json['token']
		if verify_otp(str(pk_1), otp_recv):
			if createGroup(pk_1, group_json['name']):
				return Response({'data': 'Group Saved'})
			else:
				return Response ({'data' : 'Group Data error'}, status=status.HTTP_400_BAD_REQUEST)
		else:
			return Response({'data' : 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)

class stats(APIView):

	def get(self,request,pk_1=None):
		phone_no = str(pk_1)
		otp_recv = request.GET.get('token','0')
		if verify_otp(phone_no, otp_recv):
			return Response (getStats(phone_no))
		else:
			return Response({'data' : 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
