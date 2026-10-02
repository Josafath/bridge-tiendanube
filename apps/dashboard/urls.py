from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    # Maps http://localhost:8000/ to dashboard.views.index
    path('', views.index, name='index'),
    path('test/', views.test, name="test"),
]