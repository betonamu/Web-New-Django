from django.conf.urls import url
from .views import list,post_detail
from .views import engine_search,signup
urlpatterns = [
    url(r'category/(?P<id>\d+)/$', list),
    url(r'posts/(?P<id>\d+)/$', post_detail),
    url(r'search/$', engine_search),
    url(r'', list),
] 

