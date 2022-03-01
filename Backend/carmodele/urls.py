from django.urls import path
from . import views

urlpatterns = [
	path('carmodele-list/', views.carmodeleList, name="carmodele-list"),
	path('carmodele-detail/<str:pk>/', views.carmodeleDetail, name="carmodele-detail"),
	path('carmodele-create/', views.carmodeleCreate, name="carmodele-create"),

	path('carmodele-update/<str:pk>/', views.carmodeleUpdate, name="carmodele-update"),
	path('carmodele-delete/<str:pk>/', views.carmodeleDelete, name="carmodele-delete"),
]
