from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .apiviews import PetList, UserCreate, LoginView
from rest_framework.authtoken import views

urlpatterns = [
    #path(''admin/', admin.site.urls),'
    path('pets/', PetList.as_view(), name='pet-list'),
    path('users/', UserCreate.as_view(), name='create-user'),
    path('login/', views.obtain_auth_token, name='login-view')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)