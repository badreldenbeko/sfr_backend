from rest_framework import routers
from .views import SystemViewSet

router = routers.SimpleRouter()
router.register(r'systems', SystemViewSet)
urlpatterns = router.urls
