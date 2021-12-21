from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from .views import PostList, PostDetail, PostSearch, PostListDetailfilter

app_name = 'blog_api'

# router = DefaultRouter()
# router.register(r'', PostList, basename='post')

# urlpatterns = [
#     path('', include(router.urls))
# ]

urlpatterns = [
    path('posts/', PostDetail.as_view(), name='detailcreate'),
    path('search/', PostListDetailfilter.as_view(), name='postsearch'),
    path('', PostList.as_view(), name='listcreate'),
]
