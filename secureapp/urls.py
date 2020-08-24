from rest_framework.routers import SimpleRouter
from secureapp.views import *


routers= SimpleRouter()

routers.register('employee/api/v1',EmpOperations)
routers.register('student/api/v2',StudOperations)


urlpatterns=routers.urls
