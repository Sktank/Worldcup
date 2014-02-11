__author__ = 'spencertank'
from django.conf.urls import patterns, url, include
from rest_framework import routers
from home import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'teams', views.TeamViewSet)
router.register(r'stadiums', views.StadiumViewSet)

urlpatterns = patterns('',
    url(r'^$', views.base, name='base'),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

)