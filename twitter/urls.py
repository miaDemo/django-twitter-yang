"""twitter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from accounts.api import views

import debug_toolbar

router = routers.DefaultRouter()
router.register(r'api/users', views.UserViewSet)
# 我们需要通过'/api/accounts'来访问用户的登陆状态，所以需要添加一个新的router, basename是为了避免名字冲突
router.register(r'api/accounts', views.AccountViewSet, basename='accounts')

urlpatterns = [
    path('admin/', admin.site.urls),
    # localhost 访问进来显示主页的，否则没有主页显示
    path('', include(router.urls)),
    # https://www.django-rest-framework.org/ 老师忘记干嘛的，说是直接根据官方文档设置的
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # debug toolbar
    path('__debug__/', include(debug_toolbar.urls)),
]
