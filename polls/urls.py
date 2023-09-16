from django.urls import path
from .views import GetAllFullname, PostFullname, GetDetailFullname, PatchFullname, DeleteFullname, AllFunctionFullname, PostGetFullname
from .views import GetAllLocation, GetDetailLocation, PostLocation, PatchLocation, DeleteLocation, AllFunctionLocation, PostGetLocation

urlpatterns=[
    path('GetAllFullname/', GetAllFullname.as_view()),
    path('GetDetailFullname/<int:pk>', GetDetailFullname.as_view()),
    path('PostFullname/', PostFullname.as_view() ),
    path('PatchFullname/<int:pk>', PatchFullname.as_view()),
    path('DeleteFullname/<int:pk>', DeleteFullname.as_view()),
    path('PostGetFullname/', PostGetFullname.as_view()),
    path('AllFunctionFullname/<int:pk>', AllFunctionFullname.as_view()),
    path('GetAllLocation/', GetAllLocation.as_view()),
    path('GetDetailLocation/<int:pk>', GetDetailLocation.as_view()),
    path('PostLocation/', PostLocation.as_view() ),
    path('PatchLocation/<int:pk>', PatchLocation.as_view()),
    path('DeleteLocation/<int:pk>', DeleteLocation.as_view()),
    path('PostGetLocation/', PostGetLocation.as_view()),
    path('AllFunctionLocation/<int:pk>', AllFunctionLocation.as_view())


]