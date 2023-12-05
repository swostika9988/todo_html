from django.shortcuts import render
from todoapp.models import *
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from rest_framework import status,permissions

# Create your views here.
class HomeView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request):
       userprofile = UserProfile.objects.get(user=request.user)
       ctask = Task.objects.filter(completed=True, created_by=userprofile)
       intask = Task.objects.filter(completed=False, created_by=userprofile)
       CSerializers = TaskSerializer(ctask,many=True).data
       inSerializers = TaskSerializer(intask,many=True).data
       data = {
        'completed_task' : CSerializers,
        'incompleted_task' : inSerializers,
       }
       return Response(data, status=status.HTTP_200_OK)

