from django.urls import path
from . import views

urlpatterns = [
	path('groupmember-list/', views.groupmemberList, name="groupmember-list"),
	path('groupmember-detail/<str:pk>/', views.groupmemberDetail, name="groupmember-detail"),
	path('groupmember-create/', views.groupmemberCreate, name="groupmember-create"),

	path('groupmember-update/<str:pk>/', views.groupmemberUpdate, name="groupmember-update"),
	path('groupmember-delete/<str:pk>/', views.groupmemberDelete, name="groupmember-delete"),
]
