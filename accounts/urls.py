from rest_framework import routers
from accounts.views import CustomUserViewSet


router = routers.DefaultRouter()
router.register("user", CustomUserViewSet)

urlpatterns = router.urls
