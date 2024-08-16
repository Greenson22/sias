from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .models import Teacher
from .serializer import TeacherSerializer

class TeacherViewSet(ViewSet):
     def list(self, request):
          queryset = Teacher.objects.all()
          serializer = TeacherSerializer(queryset, many=True)
          return Response(serializer.data)