from django.urls import path
from . import views

urlpatterns = [
	path('carenergy-list/', views.carenergyList, name="carenergy-list"),
	path('carenergy-detail/<str:pk>/', views.carenergyDetail, name="carenergy-detail"),
	path('carenergy-create/', views.carenergyCreate, name="carenergy-create"),

	path('carenergy-update/<str:pk>/', views.carenergyUpdate, name="carenergy-update"),
	path('carenergy-delete/<str:pk>/', views.carenergyDelete, name="carenergy-delete"),
]
