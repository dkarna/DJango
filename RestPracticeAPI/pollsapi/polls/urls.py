from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('polls/', views.PollList.as_view(), name='polls-list'),
    path('polls/<int:pk>/', views.PollDetail.as_view(), name='polls-detail'),
    path('polls/<int:pk>/choices/', views.ChoiceList.as_view(), name='choice-list'),
    path('polls/<int:pk>/choices/<int:choice_pk>/vote/', views.CreateVote.as_view(), name='create-vote'),
    path('users/', views.UserCreate.as_view(), name='user-create'),
    path('login/', views.LoginView.as_view(), name='login-view'),
]