from django.urls import path
from . import views

urlpatterns = [
	path('vote-list/', views.voteList, name="vote-list"),
	path('vote-detail/<str:pk>/', views.voteDetail, name="vote-detail"),
	path('vote-create/', views.voteCreate, name="vote-create"),

	path('vote-update/<str:pk>/', views.voteUpdate, name="vote-update"),
	path('vote-delete/<str:pk>/', views.voteDelete, name="vote-delete"),
]
