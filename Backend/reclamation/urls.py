from django.urls import path
from . import views

urlpatterns = [
	path('reclamation-list/', views.reclamationList, name="reclamation-list"),
	path('reclamation-detail/<str:pk>/', views.reclamationDetail, name="reclamation-detail"),
	path('reclamation-create/', views.reclamationCreate, name="reclamation-create"),

	path('reclamation-update/<str:pk>/', views.reclamationUpdate, name="reclamation-update"),
	path('reclamation-delete/<str:pk>/', views.reclamationDelete, name="reclamation-delete"),
]
