from django.urls import include ,path

from rest_framework import routers
# the routers from rest framework will handle requests and make sure that they end up at the correct resource dynamically
#  the router works with the viewset to route requests
# for this to work it needs to point to a viewset

from .  import views
router = routers.DefaultRouter()
router.register(r'heroes' , views.HeroViewSet)

urlpatterns = [
    path('' , include(router.urls)), 
    path('api-auth/' , include('rest_framework.urls' , namespace='rest_framework'))
]