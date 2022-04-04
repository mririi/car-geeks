from django.urls import path
from . import views

urlpatterns = [
	path('evaluation-list/', views.evaluationList, name="evaluation-list"),
	path('evaluation-detail/<str:pk>/', views.evaluationDetail, name="evaluation-detail"),
	path('evaluation-create/', views.evaluationCreate, name="evaluation-create"),

	path('evaluation-update/<str:pk>/', views.evaluationUpdate, name="evaluation-update"),
	path('evaluation-delete/<str:pk>/', views.evaluationDelete, name="evaluation-delete"),
]
