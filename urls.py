from django.urls import path
import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_weather/', views.get_weather, name='get_weather'),
]
