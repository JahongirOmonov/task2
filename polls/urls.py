from django.urls import path
from .views import getfullname, postfullname, detail


urlpatterns=[
    path('all/', getfullname.as_view()),
    path('detail/<int:myid>', detail),
    path('create/>', postfullname.as_view())
]