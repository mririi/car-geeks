from django.urls import path
from . import views

urlpatterns = [
	path('servicepromotion-list/', views.servicepromotionList, name="servicepromotion-list"),
	path('servicepromotion-detail/<str:pk>/', views.servicepromotionDetail, name="servicepromotion-detail"),
	path('servicepromotion-create/', views.servicepromotionCreate, name="servicepromotion-create"),

	path('servicepromotion-update/<str:pk>/', views.servicepromotionUpdate, name="servicepromotion-update"),
	path('servicepromotion-delete/<str:pk>/', views.servicepromotionDelete, name="servicepromotion-delete"),
]
