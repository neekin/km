# from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import LicenceSerializer
from .models import Licence

class LicenceCreateAPIView(APIView):
    def post(self, request):
        serializer = LicenceSerializer(data=request.data)
        if serializer.is_valid():
            licence = serializer.save()
            return Response({'id': licence.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class HealthCheckAPIView(APIView):
    def post(self, request):
        machine_code = request.data.get("machine_code")
        type = request.data.get("type")
        if not machine_code:
            return Response({"error": "machine_code is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            licence = Licence.objects.get(machine_code=machine_code, type=type)
            if licence.enabled == 0:
                return Response({"error": "Machine is disabled"}, status=status.HTTP_403_FORBIDDEN)
            licence.status = 1  # 设为在线
            licence.save()
            return Response({"message": "Machine status set to online"}, status=status.HTTP_200_OK)
        except Licence.DoesNotExist:
            return Response({"error": "No licence found for that machine_code"}, status=status.HTTP_404_NOT_FOUND)