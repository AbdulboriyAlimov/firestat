from pyexpat import model
from django.shortcuts import render
from django.views import generic
from requests import request
from .models import *
from news.models import *
# Create your views here.

def indexView(request):
    newslist = Post.published.all()
    fire_occ_list= object_Registration.objects.all()

    return render(request,'index.html',{'news':newslist,'events':fire_occ_list})

class PostList(generic.ListView):
    queryset = object_Registration.objects.all()
    template_name = 'fire_occ.html'

class PostDetail(generic.DeleteView):
    model = object_Registration
    template_name = 'post_detail.html'