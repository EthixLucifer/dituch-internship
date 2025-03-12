from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EntryViewSet, ProjectViewSet, ActivityViewSet, LocationViewSet, StatusViewSet

router = DefaultRouter()
router.register(r'entries', EntryViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'locations', LocationViewSet)
router.register(r'statuses', StatusViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
