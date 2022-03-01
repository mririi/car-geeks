from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BadgeSerializer

from .models import Badge
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/badge-list/',
		'Detail View':'/badge-detail/<str:pk>/',
		'Create':'/badge-create/',
		'Update':'/badge-update/<str:pk>/',
		'Delete':'/badge-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def badgeList(request):
	badges = Badge.objects.all().order_by('-id')
	serializer = BadgeSerializer(badges, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def badgeDetail(request, pk):
	badges = Badge.objects.get(id=pk)
	serializer = BadgeSerializer(badges, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def badgeCreate(request):
	serializer = BadgeSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def badgeUpdate(request, pk):
	badge = Badge.objects.get(id=pk)
	serializer = BadgeSerializer(instance=badge, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def badgeDelete(request, pk):
	badge = Badge.objects.get(id=pk)
	badge.delete()

	return Response('Item succsesfully delete!')



