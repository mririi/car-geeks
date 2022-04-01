from django.urls import path
from . import views

urlpatterns = [
	path('postgroup-list/', views.postgroupList, name="postgroup-list"),
	path('postgroup-detail/<str:pk>/', views.postgroupDetail, name="postgroup-detail"),
	path('postgroup-create/', views.postgroupCreate, name="postgroup-create"),
	path('postgroup-update/<str:pk>/', views.postgroupUpdate, name="postgroup-update"),
	path('postgroup-delete/<str:pk>/', views.postgroupDelete, name="postgroup-delete"),
]
