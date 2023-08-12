from django.shortcuts import render, redirect
from app2.models import Student
from .serializers import StudSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
import requests


class Stapi(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Student.objects.all()
        serializer = StudSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = StudSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)



def get_api(request):
    response = requests.get('http://127.0.0.1:8000/api/')
    data = response.json()
    return render(request, "getapi.html", {"data": data})



def post_api(request):
    if request.method == "POST":
        fn = request.POST.get("First Name")
        ln = request.POST.get("Last Name")
        age = request.POST.get("Age")
        term = request.POST.get("Term")
        gpa = request.POST.get("GPA")
        
        user = Student.objects.create(
                        fn=fn,
                        ln=ln,
                        age=age,
                        term=term,
                        gpa=gpa,
                        user_id=request.user.id
                        )
        user.save()
        return redirect("getapi")
    
    else:
        return render(request, "postapi.html")
