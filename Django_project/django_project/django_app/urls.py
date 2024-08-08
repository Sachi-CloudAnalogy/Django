
from django.urls import path
from . import views

urlpatterns = [
    path('', views.app_dir, name='app_dir'),
    path('<int:id>/', views.details, name='details'),
    path('form_view/', views.form_view, name='form_view'),
]
