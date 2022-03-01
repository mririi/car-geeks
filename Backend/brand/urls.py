from django.urls import path
from . import views

urlpatterns = [
	path('brand-list/', views.brandList, name="brand-list"),
	path('brand-detail/<str:pk>/', views.brandDetail, name="brand-detail"),
	path('brand-create/', views.brandCreate, name="brand-create"),

	path('brand-update/<str:pk>/', views.brandUpdate, name="brand-update"),
	path('brand-delete/<str:pk>/', views.brandDelete, name="brand-delete"),
]
