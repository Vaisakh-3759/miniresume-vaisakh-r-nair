from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Resume
from .serializers import ResumeSerializer

resume_storage = []

class heakth_check(APIView):
    def get(self, request):
        return Response({"status": "ok"}, status=status.HTTP_200_OK)

class ResumeApi(APIView):
    def post(self, request):
        serializer = ResumeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Resume added successfully.", "data": serializer.data}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        resumes = Resume.objects.all()
        serializer = ResumeSerializer(resumes, many=True)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)