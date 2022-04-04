from django.urls import path
from . import views

urlpatterns = [
	path('questioncategory-list/', views.questioncategoryList, name="questioncategory-list"),
	path('questioncategory-detail/<str:pk>/', views.questioncategoryDetail, name="questioncategory-detail"),
	path('questioncategory-create/', views.questioncategoryCreate, name="questioncategory-create"),

	path('questioncategory-update/<str:pk>/', views.questioncategoryUpdate, name="questioncategory-update"),
	path('questioncategory-delete/<str:pk>/', views.questioncategoryDelete, name="questioncategory-delete"),
]
