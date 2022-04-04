from django.urls import path
from . import views

urlpatterns = [
	path('servicetype-list/', views.servicetypeList, name="servicetype-list"),
	path('servicetype-detail/<str:pk>/', views.servicetypeDetail, name="servicetype-detail"),
	path('servicetype-create/', views.servicetypeCreate, name="servicetype-create"),

	path('servicetype-update/<str:pk>/', views.servicetypeUpdate, name="servicetype-update"),
	path('servicetype-delete/<str:pk>/', views.servicetypeDelete, name="servicetype-delete"),
]
