from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('api/state/', views.get_state, name='get_state'),
    path('api/start/', views.start_task, name='start_task'),
    path('api/reset/', views.reset_task, name='reset_task'),
    path('api/download/', views.download_output, name='download_output'),
]