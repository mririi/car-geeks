from django.urls import path
from . import views

urlpatterns = [
	path('group-list/', views.groupList, name="group-list"),
	path('group-detail/<str:pk>/', views.groupDetail, name="group-detail"),
	path('group-create/', views.groupCreate, name="group-create"),

	path('group-update/<str:pk>/', views.groupUpdate, name="group-update"),
	path('group-delete/<str:pk>/', views.groupDelete, name="group-delete"),
]
