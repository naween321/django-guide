from rest_framework.routers import DefaultRouter
from .views import ClassRoomViewSet, PersonViewSet

r = DefaultRouter()

r.register('classroom', ClassRoomViewSet, basename='classroom')
r.register('person', PersonViewSet, basename='person')

urlpatterns = r.urls
