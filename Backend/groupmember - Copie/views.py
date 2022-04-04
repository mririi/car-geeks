from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import GroupMemberSerializer

from .models import GroupMember
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/groupmember-list/',
		'Detail View':'/groupmember-detail/<str:pk>/',
		'Create':'/groupmember-create/',
		'Update':'/groupmember-update/<str:pk>/',
		'Delete':'/groupmember-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def groupmemberList(request):
	groups = GroupMember.objects.all().order_by('-id')
	serializer = GroupMemberSerializer(groups, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def groupmemberDetail(request, pk):
	groups = GroupMember.objects.get(id=pk)
	serializer = GroupMemberSerializer(groups, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def groupmemberCreate(request):
	serializer = GroupMemberSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['PUT'])
def groupmemberUpdate(request, pk):
	group = GroupMember.objects.get(id=pk)
	serializer = GroupMemberSerializer(instance=group, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def groupmemberDelete(request, pk):
	group = GroupMember.objects.get(id=pk)
	group.delete()

	return Response('Item succsesfully delete!')



