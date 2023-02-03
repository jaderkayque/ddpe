
from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'mmgd'
urlpatterns = [
    path('', views.dashboard, name='index'),
    path('estimado/', views.estimado, name='estimado'),
    #path('<int:process_id>/', views.details, name='details'),
    path(r'map/', views.map, name='map'),
]
