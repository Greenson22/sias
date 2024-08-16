from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from teacher.models import Teacher
from teacher.views import TeacherViewSet

router = DefaultRouter()
router.register('teacher', TeacherViewSet, basename='teacher')

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += router.urls
