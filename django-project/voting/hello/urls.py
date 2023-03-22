from django.urls import path
 
from . import views
urlpatterns=[
    path("",views.index,name="index"),
    path("<str:name>",views.strings,name="strings"),
    path("jeni",views.kiki,name="jeni"),
    path("",views.krishnan,name="krishnan")
]