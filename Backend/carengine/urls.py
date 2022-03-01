from django.urls import path
from . import views

urlpatterns = [
	path('carengine-list/', views.carengineList, name="carengine-list"),
	path('carengine-detail/<str:pk>/', views.carengineDetail, name="carengine-detail"),
	path('carengine-create/', views.carengineCreate, name="carengine-create"),

	path('carengine-update/<str:pk>/', views.carengineUpdate, name="carengine-update"),
	path('carengine-delete/<str:pk>/', views.carengineDelete, name="carengine-delete"),
]
