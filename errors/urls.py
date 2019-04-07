from rest_framework import routers
from .views import ErrorGroupViewSet, ErrorViewSet

router = routers.SimpleRouter()
router.register(r'errors-group', ErrorGroupViewSet)
router.register(r'errors', ErrorViewSet)
urlpatterns = router.urls
