from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('callback/', views.KindeCallbackView.as_view(), name='callback'),
]
