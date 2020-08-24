from rest_framework.serializers import ModelSerializer
from secureapp.models import Employee,Student

class EmpSerializers(ModelSerializer):
    class Meta:
        model = Employee
        fields= "__all__"



class StudSerializers(ModelSerializer):
    class Meta:
        model = Student
        fields= "__all__"
