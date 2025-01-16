# accounts/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

router = DefaultRouter()
router.register(r'accounts', UserViewSet)  # Ajoute 'users' comme préfixe 

urlpatterns = [
    path('', include(router.urls)),  # Inclut les routes générées par le DefaultRouter
]
