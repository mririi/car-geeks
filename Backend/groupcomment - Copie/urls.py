from django.urls import path
from . import views

urlpatterns = [
	path('groupcomment-list/', views.groupcommentList, name="groupcomment-list"),
	path('groupcomment-detail/<str:pk>/', views.groupcommentDetail, name="groupcomment-detail"),
	path('groupcomment-create/', views.groupcommentCreate, name="groupcomment-create"),

	path('groupcomment-update/<str:pk>/', views.groupcommentUpdate, name="groupcomment-update"),
	path('groupcomment-delete/<str:pk>/', views.groupcommentDelete, name="groupcomment-delete"),
]