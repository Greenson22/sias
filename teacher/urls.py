from django.urls import path
from .views import TeacherViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'teacher', TeacherViewSet, basename='teacher')

urlpatterns = router.urls