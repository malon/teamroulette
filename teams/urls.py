from rest_framework.routers import DefaultRouter
from . import viewsets

router = DefaultRouter()
router.register('teams', viewsets.TeamViewSet)
router.register('players', viewsets.PlayerViewSet)

urlpatterns = router.urls
