from django.contrib import admin
from django.urls import include,path
from django.conf import settings
from django.conf.urls.static import static

from Dashboard.views import login


urlpatterns=[
    path('', include('Dashboard.urls')),
    path('Dashboard/', include(('Dashboard.urls','Dashboard'),namespace = 'Dashboard')),
    path('Registration/', include('Registration.urls')),
    path('admin/', admin.site.urls)
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)