from django.urls import path
from . import views

urlpatterns = [
	path('evaluationprofile-list/', views.evaluationprofileList, name="evaluationprofile-list"),
	path('evaluationprofile-detail/<str:pk>/', views.evaluationprofileDetail, name="evaluationprofile-detail"),
	path('evaluationprofile-create/', views.evaluationprofileCreate, name="evaluationprofile-create"),

	path('evaluationprofile-update/<str:pk>/', views.evaluationprofileUpdate, name="evaluationprofile-update"),
	path('evaluationprofile-delete/<str:pk>/', views.evaluationprofileDelete, name="evaluationprofile-delete"),
]
