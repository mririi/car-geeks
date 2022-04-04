from django.urls import path
from . import views

urlpatterns = [
	path('groupvote-list/', views.groupvoteList, name="groupvote-list"),
	path('groupvote-detail/<str:pk>/', views.groupvoteDetail, name="groupvote-detail"),
	path('groupvote-create/', views.groupvoteCreate, name="groupvote-create"),

	path('groupvote-update/<str:pk>/', views.groupvoteUpdate, name="groupvote-update"),
	path('groupvote-delete/<str:pk>/', views.groupvoteDelete, name="groupvote-delete"),
]
