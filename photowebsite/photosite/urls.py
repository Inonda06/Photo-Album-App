from django.urls import path
from .import views


urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('add/', views.addPhoto, name='add'),
    path('Pictures/<str:pk>/', views.Pictures, name='Pictures'),
]