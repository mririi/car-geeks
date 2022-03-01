from django.urls import path
from . import views

urlpatterns = [
	path('preferences-list/', views.preferencesList, name="preferences-list"),
	path('preferences-detail/<str:pk>/', views.preferencesDetail, name="preferences-detail"),
	path('preferences-create/', views.preferencesCreate, name="preferences-create"),

	path('preferences-update/<str:pk>/', views.preferencesUpdate, name="preferences-update"),
	path('preferences-delete/<str:pk>/', views.preferencesDelete, name="preferences-delete"),
]
