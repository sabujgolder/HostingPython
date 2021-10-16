from django.urls import path
from . import views

app_name = "myapp"

urlpatterns = [
    path('artists/',views.artists,name='artists'),
    path('about/<int:artist_id>/',views.about,name='about'),
    path('index/',views.index,name='index'),
    path('form/',views.forms,name='form'),
]
