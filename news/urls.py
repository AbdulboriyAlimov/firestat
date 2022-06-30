from django.urls import path
from . import views

app_name = 'news'

urlpatterns=[
    path('',views.post_list, name='all_news'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',views.post_detail,name='news_details'),
]