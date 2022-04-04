from django.urls import path
from . import views

urlpatterns = [
	path('question-list/', views.questionList, name="question-list"),
	path('question-detail/<str:pk>/', views.questionDetail, name="question-detail"),
	path('question-create/', views.questionCreate, name="question-create"),

	path('question-update/<str:pk>/', views.questionUpdate, name="question-update"),
	path('question-delete/<str:pk>/', views.questionDelete, name="question-delete"),
]
