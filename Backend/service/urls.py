from django.urls import path
from . import views

urlpatterns = [
	path('service-list/', views.serviceList, name="service-list"),
	path('service-detail/<str:pk>/', views.serviceDetail, name="service-detail"),
	path('service-create/', views.serviceCreate, name="service-create"),

	path('service-update/<str:pk>/', views.serviceUpdate, name="service-update"),
	path('service-delete/<str:pk>/', views.serviceDelete, name="service-delete"),
]
