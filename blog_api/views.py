from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer
from rest_framework.permissions import SAFE_METHODS, BasePermission, IsAdminUser, DjangoModelPermissions, IsAuthenticated

# https://www.django-rest-framework.org/api-guide/permissions/

class PostUserWritePermission(BasePermission):
    message = 'Editing posts is restricted to the author only!'

    def has_object_permission(self, request, view, obj):
        # obj -> Post Object
        return obj.author == request.user or IsAdminUser.has_permission(self, request, view)


class PostList(generics.ListCreateAPIView):
    permission_classes = (IsAdminUser|IsAuthenticated, ) # isAdmin or ...
    queryset = Post.postobjects.all() # return all Posts that are flagged as 'published' -> check Model Post -> PostObjetcs
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
    permission_classes = [PostUserWritePermission] # isAdmin or ...
    queryset = Post.objects.all() # return all Posts that are flagged as 'published' -> check Model Post -> PostObjetcs
    serializer_class = PostSerializer

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
