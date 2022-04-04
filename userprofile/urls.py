from django.urls import path
from . import views

urlpatterns = [
	path('userprofile-list/', views.userprofileList, name="userprofile-list"),
	path('userprofile-detail/<str:pk>/', views.userprofileDetail, name="userprofile-detail"),
	path('userprofile-create/', views.userprofileCreate, name="userprofile-create"),

	path('userprofile-update/<str:pk>/', views.userprofileUpdate, name="userprofile-update"),
	path('userprofile-delete/<str:pk>/', views.userprofileDelete, name="userprofile-delete"),
]
