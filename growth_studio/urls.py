"""growth_studio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from graphene_django.views import GraphQLView

from blog.api import BlogSet, UserDetail
from blog.views import blog_list, blog_detail
from homepage.views import index as home

from rest_framework import routers
from rest_framework_jwt import views as DRFViews

apiRouter = routers.DefaultRouter()
apiRouter.register(r'blog', BlogSet, 'blog')
apiRouter.register(r'user', UserDetail, 'user')

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^pages/about-us/$', TemplateView.as_view(template_name='flatpages/about-us.html')),
    url(r'^blog/$', blog_list),
    url(r'^blog/(?P<slug>[^\.]+).html', blog_detail, name='blog_view'),
    url(r'^admin/', admin.site.urls),
    url(r'^graphql', GraphQLView.as_view(graphiql=True)),
    url('^markdown/', include('django_markdown.urls')),
    url(r'^api/', include(apiRouter.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', DRFViews.obtain_jwt_token),
    url(r'^api-token-refresh/', DRFViews.refresh_jwt_token),
    url(r'^api-token-verify/', DRFViews.verify_jwt_token),
]
