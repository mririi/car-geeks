from django.urls import path
from . import views

urlpatterns = [
	path('chat-list/', views.chatList, name="chat-list"),
	path('chat-detail/<str:pk>/', views.chatDetail, name="chat-detail"),
	path('chat-create/', views.chatCreate, name="chat-create"),

	path('chat-update/<str:pk>/', views.chatUpdate, name="chat-update"),
	path('chat-delete/<str:pk>/', views.chatDelete, name="chat-delete"),
]
