
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('GlavApp.urls')),
    path('about', include('GlavApp.urls')),
]
