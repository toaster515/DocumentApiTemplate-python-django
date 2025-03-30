from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FileRecordViewSet

router = DefaultRouter()
router.register(r'files', FileRecordViewSet)

urlpatterns = [
    path('', include(router.urls)),
]