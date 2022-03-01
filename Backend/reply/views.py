from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ReplySerializer

from .models import Reply
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/reply-list/',
		'Detail View':'/reply-detail/<str:pk>/',
		'Create':'/reply-create/',
		'Update':'/reply-update/<str:pk>/',
		'Delete':'/reply-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def replyList(request):
	replys = Reply.objects.all().order_by('id')
	serializer = ReplySerializer(replys, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def replyDetail(request, pk):
	replys = Reply.objects.get(id=pk)
	serializer = ReplySerializer(replys, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def replyCreate(request):
	serializer = ReplySerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def replyUpdate(request, pk):
	reply = Reply.objects.get(id=pk)
	serializer = ReplySerializer(instance=reply, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def replyDelete(request, pk):
	reply = Reply.objects.get(id=pk)
	reply.delete()

	return Response('Item succsesfully delete!')



