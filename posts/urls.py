from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'feed', views.FeedView)
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)


urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'base_layout', views.base_layout, name='base_layout'),
    path(r'getdata', views.getdata, name='getdata'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
