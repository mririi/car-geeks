from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
from django.views.generic import View
from django.shortcuts import redirect
from django.contrib import messages
from django.core.mail import send_mail, send_mass_mail 
from django.shortcuts import render
from django.http import JsonResponse
from .serializers import EmailSerializer

from .models import Email
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/email-list/',
		'Detail View':'/email-detail/<str:pk>/',
		'Create':'/email-create/',
		'Update':'/email-update/<str:pk>/',
		'Delete':'/email-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def emailList(request):
	emails = Email.objects.all().order_by('id')
	serializer = EmailSerializer(emails, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def emailDetail(request, pk):
	emails = Email.objects.get(id=pk)
	serializer = EmailSerializer(emails, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def emailCreate(request):
	serializer = EmailSerializer(data=request.data)
	if serializer.is_valid():
         serializer.save()
         send_mail(str(request.data.get('subject')), str(request.data.get('message')), 'fruine6@gmail.com', [str(request.data.get('to'))], fail_silently=False)
         return Response(request.data)

@api_view(['POST'])
def emailUpdate(request, pk):
	email = Email.objects.get(id=pk)
	serializer = EmailSerializer(instance=email, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def emailDelete(request, pk):
	email = Email.objects.get(id=pk)
	email.delete()
	return Response('Item succsesfully delete!')



