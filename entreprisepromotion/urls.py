from django.urls import path
from . import views

urlpatterns = [
	path('entreprisepromotion-list/', views.entreprisepromotionList, name="entreprisepromotion-list"),
	path('entreprisepromotion-detail/<str:pk>/', views.entreprisepromotionDetail, name="entreprisepromotion-detail"),
	path('entreprisepromotion-create/', views.entreprisepromotionCreate, name="entreprisepromotion-create"),

	path('entreprisepromotion-update/<str:pk>/', views.entreprisepromotionUpdate, name="entreprisepromotion-update"),
	path('entreprisepromotion-delete/<str:pk>/', views.entreprisepromotionDelete, name="entreprisepromotion-delete"),
]
