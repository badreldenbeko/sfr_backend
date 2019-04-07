from rest_framework import routers
from .views import BranchViewSet

router = routers.SimpleRouter()
router.register(r'branches', BranchViewSet)
urlpatterns = router.urls
