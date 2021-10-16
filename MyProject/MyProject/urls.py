from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.base,name='base'),
    path('appone/',include('myapp.urls')),
    path('apptwo/',include('myapp2.urls')),
]
