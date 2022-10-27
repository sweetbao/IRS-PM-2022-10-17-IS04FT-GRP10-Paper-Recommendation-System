"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers
from PaperRecommend.views import PaperViewSet,addData
from account import views
from account.views import UserPreferViewSet, UserRecordViewSet


router = routers.DefaultRouter()
router.register(r'PaperRecommend', PaperViewSet)
router.register(r'UserPrefer', UserPreferViewSet)
router.register(r'ViewRecord', UserRecordViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
    path('testAdd',addData),
    path('register/',views.Register.as_view()),
    path('login/',views.Login.as_view()),
]
