from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from secureapp.models import Employee,Student
from secureapp.serializer import EmpSerializers,StudSerializers
from rest_framework.permissions import *
from django.contrib.auth.models import User

class CustomPermissions(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser) and self.has_object_permission(request,None,None)


    def has_object_permission(self, request, view, obj):
        info = request.data
        data = info.get('desig')
        if data == 'Manager':
            return True
        return False


class EmpOperations(ModelViewSet):
    permission_classes = (CustomPermissions,)
    queryset = Employee.objects.all()
    serializer_class = EmpSerializers

    def get_permissions(self):
        if self.action == 'list':
            self.permission_classes = (IsAdminUser,)
        return super().get_permissions()

class StudOperations(ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = Student.objects.all()
    serializer_class = StudSerializers

