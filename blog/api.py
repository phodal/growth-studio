from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import serializers, viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import BasePermission
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from blog.models import Blog

SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS']


class IsAuthenticatedOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if (request.method in SAFE_METHODS or
                    request.user and
                    request.user.is_authenticated()):
            return True
        return False


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')


class BlogSerializer(serializers.ModelSerializer):
    author = User

    class Meta:
        model = Blog
        fields = ('title', 'author', 'body', 'slug', 'id')


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10


class BlogSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = Blog.objects.all()
        title = self.request.query_params.get('title', None)
        if title is not None:
            queryset = queryset.filter(title__contains=title)
        return queryset

class UserDetail(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [JSONWebTokenAuthentication, BasicAuthentication, SessionAuthentication]
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
