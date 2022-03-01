from django.urls import path
from . import views

urlpatterns = [
	path('userentreprise-list/', views.userentrepriseList, name="userentreprise-list"),
	path('userentreprise-detail/<str:pk>/', views.userentrepriseDetail, name="userentreprise-detail"),
	path('userentreprise-create/', views.userentrepriseCreate, name="userentreprise-create"),

	path('userentreprise-update/<str:pk>/', views.userentrepriseUpdate, name="userentreprise-update"),
	path('userentreprise-delete/<str:pk>/', views.userentrepriseDelete, name="userentreprise-delete"),
]
