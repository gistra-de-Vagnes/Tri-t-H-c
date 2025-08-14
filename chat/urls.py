from django.urls import path
from . import views

app_name = 'discussions'

urlpatterns = [
    path('', views.discussions_home, name='home'),
    path('category/<int:pk>/', views.category_detail, name='category_detail'),
    path('topic/<int:pk>/', views.topic_detail, name='topic_detail'),
    path('category/<int:category_pk>/create-topic/', views.create_topic, name='create_topic'),
    path('topic/<int:topic_pk>/reply/', views.create_reply, name='create_reply'),
]