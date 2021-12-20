from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter

from .views import PostList

app_name = 'blog_api'

router = DefaultRouter()
router.register(r'', PostList, basename='post')

urlpatterns = [
    path('', include(router.urls))
]

# urlpatterns = [
#    path('<int:pk>/', PostDetail.as_view(), name="detailcreate"),
#    path('', PostList.as_view(), name="listcreate")
# ]
