from django.conf.urls import url, include
from . import views
#from blog.models import Post

urlpatterns = [ url(r'^$', views.index, name='index')]