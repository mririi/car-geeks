from django.urls import path
from . import views

urlpatterns = [
	path('email-list/', views.emailList, name="email-list"),
	path('email-detail/<str:pk>/', views.emailDetail, name="email-detail"),
	path('email-create/', views.emailCreate, name="email-create"),

	path('email-update/<str:pk>/', views.emailUpdate, name="email-update"),
	path('email-delete/<str:pk>/', views.emailDelete, name="email-delete"),
]
