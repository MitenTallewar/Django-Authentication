
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view
# from secureapp.views import get_token
from rest_framework.authtoken import views
schema_view = get_swagger_view(title='Secure API by Miten')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employee/',include('secureapp.urls')),
    # path('student/',include('authapp.urls')),
    path('api-auth',include('rest_framework.urls')),
    url(r'swagger/',schema_view),
    # path('auth/', include('rest_authtoken.urls')),
    path('token/',views.obtain_auth_token)#will call to get token (inbuilt method)
]
