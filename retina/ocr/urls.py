from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('upload/', views.upload, name='upload'),
    path('signup/', views.signup, name='signup'),
    path('document_view/', views.view_document, name='document_view')

]
