from blog.models import Post
from django.conf import settings
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['category', 'id', 'title', 'image', 'slug', 'author',
                  'excerpt', 'content', 'status']


class UserRegisterSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ('email', 'user_name', 'first_name')
        extra_kwargs = {'password': {'write_only': True}}


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['user_name'] = user.user_name
        token['first_name'] = user.first_name
        token['is_superuser'] = user.is_superuser
        print('Token from MyTokenObtainPairSerializer', user.email)
        return token

    def validate(self, attrs):
        print('VALIDATE Token Attrs', attrs)
        data = super(MyTokenObtainPairSerializer, self).validate(attrs)
        print('#####################################################')
        print('VALIDATE Token Data', self)

        data['user'] = {
            'user_name': self.user.user_name,
            'id': self.user.id,
            'first_name': self.user.first_name,
            'is_superuser': self.user.is_superuser
        }

        return data
