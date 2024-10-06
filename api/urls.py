from rest_framework.routers import DefaultRouter
from django.urls import path, re_path, include

from . import views
from .views import ShortenViewSet

router = DefaultRouter()
router.register(r'shorten', ShortenViewSet, basename='shorten')

urlpatterns = [
    path('', include(router.urls)),

    # Custom path for the 8-character code
    path('<str:code>/', views.my_redirect_view, name='redirect-view'),
]
