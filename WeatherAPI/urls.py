from django.contrib import admin
from django.urls import path, include
from weatherapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('weatherapp.urls')),
]
