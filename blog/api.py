from django.contrib.auth.models import User
from rest_framework import serializers, viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import BasePermission
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from rest_framework import permissions
from blog.models import Blog

SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS']


class IsAuthenticatedOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if (request.method in SAFE_METHODS or
                    request.user and
                    request.user.is_authenticated()):
            return True
        return False


class BlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blog
        fields = ('title', 'body', 'slug', 'id')


class BlogSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = BlogSerializer
    search_fields = 'title'

    def get_queryset(self):
        return Blog.objects.all()

    def list(self, request):
        queryset = Blog.objects.all()

        search_param = self.request.query_params.get('title', None)
        if search_param is not None:
            queryset = Blog.objects.filter(title__contains=search_param)

        serializer = BlogSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)
