
from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import NotificationsSerializer

from .models import Notifications
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/notification-list/',
		'Detail View':'/notification-detail/<str:pk>/',
		'Create':'/notification-create/',
		'Update':'/notification-update/<str:pk>/',
		'Delete':'/notification-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def notificationList(request):
	notifications = Notifications.objects.all().order_by('-id')
	serializer = NotificationsSerializer(notifications, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def notificationDetail(request, pk):
	notifications = Notifications.objects.get(id=pk)
	serializer = NotificationsSerializer(notifications, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def notificationCreate(request):
	serializer = NotificationsSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['PUT'])
def notificationUpdate(request, pk):
	notification = Notifications.objects.get(id=pk)
	serializer = NotificationsSerializer(instance=notification, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def notificationDelete(request, pk):
	notification = Notifications.objects.get(id=pk)
	notification.delete()

	return Response('Item succsesfully delete!')



