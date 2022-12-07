from django.urls import path
from .import views

urlpatterns=[
    path('myhome/',views.getahome,name="home"),
    path('myprojects/',views.getaprojects,name="projects"),
    path('myprofiles',views.getaprofiles,name="profile"),
    path('my profiles2',views.getaprofiles2,name="profile2")
]

