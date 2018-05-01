from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('build/<int:pk>', views.view_build, name='build'),
    path('new/', views.create_build, name='build_new'),
]