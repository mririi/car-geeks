from django.urls import path
from . import views

urlpatterns = [
	path('reply-list/', views.replyList, name="reply-list"),
	path('reply-detail/<str:pk>/', views.replyDetail, name="reply-detail"),
	path('reply-create/', views.replyCreate, name="reply-create"),

	path('reply-update/<str:pk>/', views.replyUpdate, name="reply-update"),
	path('reply-delete/<str:pk>/', views.replyDelete, name="reply-delete"),
]
