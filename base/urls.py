from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('listing/', views.listing, name='listing'),
    path('property/<int:pk>/', views.property, name='property'),
    path('agent/', views.agent, name='agent'),
    path('blog_single/', views.blog_single, name='blog_single'),    
    path('agent_single/', views.agent_single, name='agent_single'),
]
