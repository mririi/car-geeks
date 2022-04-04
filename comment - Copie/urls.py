from django.urls import path
from . import views

urlpatterns = [
	path('comment-list/', views.commentList, name="comment-list"),
	path('comment-detail/<str:pk>/', views.commentDetail, name="comment-detail"),
	path('comment-create/', views.commentCreate, name="comment-create"),

	path('comment-update/<str:pk>/', views.commentUpdate, name="comment-update"),
	path('comment-delete/<str:pk>/', views.commentDelete, name="comment-delete"),
]
