from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('voting', views.display, name='display'),
    path('voting', views.vote, name='vote'),
    
]