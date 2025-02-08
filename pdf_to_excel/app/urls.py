from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='base'),
    path('upload/', views.upload_doc, name='upload')
]
