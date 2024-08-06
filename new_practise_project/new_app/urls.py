from django.urls import path
from new_app import views

urlpatterns = [path('hello-view/', views.HelloApiView.as_view()),]
