from django.urls import path
from api.views import UpdateModelDetailAPIView, UpdateModelListAPIView

urlpatterns = [
    path('', UpdateModelListAPIView.as_view()),
    path('<int:id>/', UpdateModelDetailAPIView.as_view()), 
]
