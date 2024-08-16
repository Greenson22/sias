from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from teacher.models import Teacher
from teacher.views import TeacherViewSet

router = DefaultRouter()
router.register('teacher', TeacherViewSet, basename='teacher')

urlpatterns = [
    path('admin/', admin.site.urls),
]

# menambahkan url dari Teacer ViewSet
urlpatterns += router.urls

# jika di mode debug maka masukan url dari media
if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)