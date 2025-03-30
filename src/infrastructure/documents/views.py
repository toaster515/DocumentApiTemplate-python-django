from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import FileRecord
from .serializers import FileRecordSerializer
from application.file_services import handle_file_upload

class FileRecordViewSet(viewsets.ModelViewSet):
    queryset = FileRecord.objects.all()
    serializer_class = FileRecordSerializer

    def create(self, request):
        file = request.FILES.get('file')
        provider = request.data.get('provider')

        if not file or not provider:
            return Response({'error': 'File and provider are required.'}, status=status.HTTP_400_BAD_REQUEST)

        result = handle_file_upload(file, provider)
        return Response(result, status=status.HTTP_201_CREATED)