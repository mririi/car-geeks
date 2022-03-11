from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/',include('userapi.urls')),
    path('question/',include('question.urls')),
    path('badge/',include('badge.urls')),
    path('questioncategory/',include('questioncategory.urls')),
    path('comment/',include('comment.urls')),
    path('evaluation/',include('evaluation.urls')),
    path('preferences/',include('preferences.urls')),
    path('reclamation/',include('reclamation.urls')),
    path('notification/',include('notifications.urls')),
    path('reply/',include('reply.urls')),
    path('role/',include('role.urls')),
    path('service/',include('service.urls')),
    path('servicetype/',include('servicetype.urls')),
    path('userprofile/',include('userprofile.urls')),
    path('car/',include('car.urls')),
    path('vote/',include('vote.urls')),
    path('userentreprise/',include('userentreprise.urls')),
    path('auth/', obtain_auth_token),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)