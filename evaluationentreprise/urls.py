from django.urls import path
from . import views

urlpatterns = [
	path('evaluationentreprise-list/', views.evaluationentrepriseList, name="evaluationentreprise-list"),
	path('evaluationentreprise-detail/<str:pk>/', views.evaluationentrepriseDetail, name="evaluationentreprise-detail"),
	path('evaluationentreprise-create/', views.evaluationentrepriseCreate, name="evaluationentreprise-create"),

	path('evaluationentreprise-update/<str:pk>/', views.evaluationentrepriseUpdate, name="evaluationentreprise-update"),
	path('evaluationentreprise-delete/<str:pk>/', views.evaluationentrepriseDelete, name="evaluationentreprise-delete"),
]
