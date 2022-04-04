from django.urls import path
from . import views

urlpatterns = [
	path('role-list/', views.roleList, name="role-list"),
	path('role-detail/<str:pk>/', views.roleDetail, name="role-detail"),
	path('role-create/', views.roleCreate, name="role-create"),

	path('role-update/<str:pk>/', views.roleUpdate, name="role-update"),
	path('role-delete/<str:pk>/', views.roleDelete, name="role-delete"),
]
