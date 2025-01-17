from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name="home"),
    path('addmusician', views.addmusician, name="addmusician"),
    path('addalbum', views.addalbum, name="addalbum"),
    path('updatealbum', views.updatealbum, name="updatealbum"),
    path('deletealbum', views.deletealbum, name="deletealbum"),
    path('updatemusician', views.updatemusician, name="updatemusician"),
    path('deletemusician', views.deletemusician, name="deletemusician"),
    path('admin/', admin.site.urls),
]
