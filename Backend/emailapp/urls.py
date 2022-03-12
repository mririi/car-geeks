from django.urls import path
from . import views

urlpatterns = [
	path('emailer/', views.SendFormEmail.as_view(), name="send-email"),
]
