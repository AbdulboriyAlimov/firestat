from . import views
from django.urls import path

app_name= 'eguide'
urlpatterns = [
    path('', views.indexView , name='index'),
    path('fire_events/',views.PostList.as_view(), name='home'),
    path('fire_events/<int:pk>/',views.PostDetail.as_view(),name='post_detail'),
]