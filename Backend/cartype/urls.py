from django.urls import path
from . import views

urlpatterns = [
	path('cartype-list/', views.cartypeList, name="cartype-list"),
	path('cartype-detail/<str:pk>/', views.cartypeDetail, name="cartype-detail"),
	path('cartype-create/', views.cartypeCreate, name="cartype-create"),

	path('cartype-update/<str:pk>/', views.cartypeUpdate, name="cartype-update"),
	path('cartype-delete/<str:pk>/', views.cartypeDelete, name="cartype-delete"),
]
