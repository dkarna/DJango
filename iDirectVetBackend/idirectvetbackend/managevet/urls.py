from django.template.backends import django
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
#from .apiviews import PetList, UserCreate, LoginView, UserViewSet
#from rest_framework.authtoken import views
from . import apiviews as vetviews
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users',vetviews.UserViewSet, basename='user-view')
router.register(r'pets', vetviews.PetViewSet, basename='pet-view')
router.register(r'profile', vetviews.ProfileViewSet, basename='profile-view')

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #path('api/auth/', include('djoser.urls.authtoken')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)