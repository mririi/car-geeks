from django.urls import path
from . import views

urlpatterns = [
	path('car-list/', views.carList, name="car-list"),
	path('car-detail/<str:pk>/', views.carDetail, name="car-detail"),
	path('car-create/', views.carCreate, name="car-create"),

	path('car-update/<str:pk>/', views.carUpdate, name="car-update"),
	path('car-delete/<str:pk>/', views.carDelete, name="car-delete"),
]
