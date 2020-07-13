from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns= [
    url('',views.index,name= 'index'),
    path("create-new-project/", views.createnewproj, name="create new project"),
]