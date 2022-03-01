from django.urls import path
from . import views

urlpatterns = [
	path('badge-list/', views.badgeList, name="badge-list"),
	path('badge-detail/<str:pk>/', views.badgeDetail, name="badge-detail"),
	path('badge-create/', views.badgeCreate, name="badge-create"),

	path('badge-update/<str:pk>/', views.badgeUpdate, name="badge-update"),
	path('badge-delete/<str:pk>/', views.badgeDelete, name="badge-delete"),
]
