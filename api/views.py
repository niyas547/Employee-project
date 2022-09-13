from django.shortcuts import render
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework.response import Response
from api.serializers import EmployeeSerializer,UserSerializer
from api.models import Employee
from rest_framework import authentication,permissions
# Create your views here.

class EmployeeView(ViewSet):
    # authentication_classes =[authentication.BasicAuthentication]
    authentication_classes =[authentication.TokenAuthentication]
    permission_classes =[permissions.IsAuthenticated]

    def list(self,request,*args,**kwargs):
        qs=Employee.objects.all()
        serializer=EmployeeSerializer(qs,many=True)
        return Response(data=serializer.data)
    def create(self,request,*args,**kwargs):
        serializer=EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Employee.objects.get(id=id)
        serializer=EmployeeSerializer(qs)
        return Response(data=serializer.data)
    def update(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Employee.objects.get(id=id)
        serializer=EmployeeSerializer(instance=qs,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    def destroy(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Employee.objects.get(id=id)
        qs.delete()
        return Response({"message":"deleted"})

class UsersView(ViewSet):
    def create(self,request,*args,**kwargs):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)



class EmployeeModelView(ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]



