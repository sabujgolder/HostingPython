from django.urls import path,include
from myapp2 import views

app_name = "myapp2"
urlpatterns = [
    path('',views.home,name='home'),
    path('modelform',views.NewUserForm,name='modelform'),
]
