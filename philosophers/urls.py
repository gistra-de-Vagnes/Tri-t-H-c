from django.urls import path
from . import views
from . import views_registration

app_name = 'philosophers'

urlpatterns = [
    path('', views.home, name='home'),
    path('philosophers/', views.philosopher_list, name='philosopher_list'),
    path('philosophers/<int:pk>/', views.philosopher_detail, name='philosopher_detail'),
    path('schools/', views.school_list, name='school_list'),
    path('schools/<int:pk>/', views.school_detail, name='school_detail'),
    path('api/philosophers/<int:pk>/', views.get_philosopher_data, name='philosopher_api'),
    path('api/search/', views.search_philosophers_api, name='search_api'),
    path('register/', views_registration.register, name='register'),
    path('profile/', views_registration.profile, name='profile'),
]