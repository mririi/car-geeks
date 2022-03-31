from django.shortcuts import render
from django.http import JsonResponse
from .pusher import pusher_client
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ChatSerializer

from .models import Chat
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/chat-list/',
		'Detail View':'/chat-detail/<str:pk>/',
		'Create':'/chat-create/',
		'Update':'/chat-update/<str:pk>/',
		'Delete':'/chat-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def chatList(request):
	chats = Chat.objects.all().order_by('id')
	serializer = ChatSerializer(chats, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def chatDetail(request, pk):
	chats = Chat.objects.get(id=pk)
	serializer = ChatSerializer(chats, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def chatCreate(request):
	serializer = ChatSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()
		pusher_client.trigger('chat', 'messagee',{'chat':request.data})

	return Response(request.data)

@api_view(['POST'])
def chatUpdate(request, pk):
	chat = Chat.objects.get(id=pk)
	serializer = ChatSerializer(instance=chat, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def chatDelete(request, pk):
	chat = Chat.objects.get(id=pk)
	chat.delete()

	return Response('Item succsesfully delete!')



