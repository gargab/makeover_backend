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
from makeoverapp.v1.OTP.otp import *
from makeoverapp.v1.OTP.verify_otp import *
from makeoverapp.v1.SMS.send_sms import *

class user(APIView):

	def post(self,request,pk_1 = None,pk_2 = None):
		user_json  = request.data
		otp_recv = user_json['token']
		user_json['phone_number']=str(pk_2)
		user_json['created_by'] = str(pk_1)
		if verify_otp(str(pk_1), otp_recv):
			if createUser(user_json):
				return Response ({'data' : 'User Added'})

			else:
				return Response ({'data' : 'Invalid Data'})
		else:
			return Response({'data' : 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)


class group(APIView):

	def post(self,request,pk_1 = None):
		group_json  = request.data
		otp_recv = user_json['token']
		if verify_otp(str(pk_1), otp_recv):
			group_json['created_by']=str(pk_1)
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
