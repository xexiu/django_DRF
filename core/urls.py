from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('darvel.urls', namespace='darvel')),
    path('api/', include('darvel_api.urls', namespace='darvel_api')),
    path('admin/', admin.site.urls),
]
