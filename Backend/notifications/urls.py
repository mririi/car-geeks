from django.urls import path
from . import views

urlpatterns = [
	path('notification-list/', views.notificationList, name="notification-list"),
	path('notification-detail/<str:pk>/', views.notificationDetail, name="notification-detail"),
	path('notification-create/', views.notificationCreate, name="notification-create"),

	path('notification-update/<str:pk>/', views.notificationUpdate, name="notification-update"),
	path('notification-delete/<str:pk>/', views.notificationDelete, name="notification-delete"),
]