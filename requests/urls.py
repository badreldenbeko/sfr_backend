from rest_framework import routers
from .views import RequestViewSetCreate, RequestViewSetRead

router = routers.SimpleRouter()
router.register(r'requests', RequestViewSetRead)
router.register(r'requests-create', RequestViewSetCreate)
urlpatterns = router.urls
