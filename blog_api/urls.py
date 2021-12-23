from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter

from .views import (AdminPostDetail, CreatePost, EditPost, PostDetail,
                    PostList, PostSearch, DeletePost)

app_name = 'blog_api'

# router = DefaultRouter()
# router.register(r'', PostList, basename='post')

# urlpatterns = [
#     path('', include(router.urls))
# ]

urlpatterns = [
    path('', PostList.as_view(), name='listpost'),
    path('post/<int:pk>/', PostDetail.as_view(), name='detailpost'),
    path('search/', PostSearch.as_view(), name='postsearch'),
    # Post Admin URLs
    path('admin/create/', CreatePost.as_view(), name='createpost'),
    path('admin/edit/postdetail/<int:pk>/',
         AdminPostDetail.as_view(), name='admindetailpost'),
    path('admin/edit/<int:pk>/', EditPost.as_view(), name='editpost'),
    path('admin/delete/<int:pk>/', DeletePost.as_view(), name='deletepost')
]
