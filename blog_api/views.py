from blog.models import Post
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import generics, viewsets, filters
from rest_framework.permissions import (SAFE_METHODS, AllowAny, BasePermission,
                                        DjangoModelPermissions, IsAdminUser,
                                        IsAuthenticated)
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import MyTokenObtainPairSerializer, PostSerializer

# https://www.django-rest-framework.org/api-guide/permissions/


class PostUserWritePermission(BasePermission):
    message = 'Editing posts is restricted to the author only!'

    def has_object_permission(self, request, view, obj):
        # obj -> Post Object
        return obj.author == request.user or IsAdminUser.has_permission(self, request, view)

class PostList(generics.ListAPIView):
    print('HEYYYYY AUTH')
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.postobjects.all()


class PostDetail(generics.ListAPIView):
    serializer_class = PostSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        slug = self.request.query_params.get('slug', None)
        print('SLUG:', slug)
        return Post.objects.filter(slug=slug)


class PostListDetailfilter(generics.ListAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^slug']

    # '^' Starts-with search.
    # '=' Exact matches.
    # '@' Full-text search. (Currently only supported Django's PostgreSQL backend.)
    # '$' Regex search.


class PostSearch(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^slug']


# class PostList(viewsets.ModelViewSet):
#     permission_classes = [IsAuthenticated]
#     serializer_class = PostSerializer
#     queryset = Post.postobjects.all()

#     def get_object(self, queryset=None, **kwargs):
#         item_id = self.kwargs.get('pk')
#         print('Post Item: ', item_id)
#         return get_object_or_404(self.queryset, id=item_id)


# class PostList(viewsets.ViewSet):
#     permission_classes = [PostUserWritePermission]
#     queryset = Post.postobjects.all()

#     def list(self, request):
#         serializer_class = PostSerializer(self.queryset, many=True)
#         return Response(serializer_class.data)

#     def create(self, request):
#         pass

#     def retrieve(self, request, pk=None):
#         post = get_object_or_404(self.queryset, slug=pk)
#         serializer_class = PostSerializer(post)
#         return Response(serializer_class.data)

#     def update(self, request, pk=None):
#         pass

#     def partial_update(self, request, pk=None):
#         pass

#     def destroy(self, request, pk=None):
#         pass

#     pass


# class PostList(generics.ListCreateAPIView):
#     permission_classes = [IsAuthenticated] # isAdmin or ...
#     queryset = Post.postobjects.all() # return all Posts that are flagged as 'published' -> check Model Post -> PostObjetcs
#     serializer_class = PostSerializer

# class PostDetail(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
#     permission_classes = [PostUserWritePermission]
#     queryset = Post.objects.all() # return all Posts
#     serializer_class = PostSerializer

class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = [AllowAny]
    serializer_class = MyTokenObtainPairSerializer
    print('HEYYY Token from MyObtainTokenPairView', serializer_class)


"""
#### PERMISSIONS ####
- We have some different options when adding permissions
1. On project wide
2. On a view
3. On an object
4. Custom Permissions
"""

""" Concrete View Classes
#CreateAPIView
Used for create-only endpoints.
#ListAPIView
Used for read-only endpoints to represent a collection of model instances.
#RetrieveAPIView
Used for read-only endpoints to represent a single model instance.
#DestroyAPIView
Used for delete-only endpoints for a single model instance.
#UpdateAPIView
Used for update-only endpoints for a single model instance.
##ListCreateAPIView
Used for read-write endpoints to represent a collection of model instances.
RetrieveUpdateAPIView
Used for read or update endpoints to represent a single model instance.
#RetrieveDestroyAPIView
Used for read or delete endpoints to represent a single model instance.
#RetrieveUpdateDestroyAPIView
Used for read-write-delete endpoints to represent a single model instance.
"""
