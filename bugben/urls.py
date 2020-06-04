from django.contrib import admin
from django.urls import path
from resume.views import resume

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', resume),
]
