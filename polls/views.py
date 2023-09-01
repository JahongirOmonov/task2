from django.shortcuts import render, get_object_or_404
from .models import fullname, location
from django.http import JsonResponse
from .serializer import fullnameSerializer, locationSerializer

# Create your views here.

def all(request):
    all=fullname.objects.all()
    mylist =fullnameSerializer(all, many=True)
    # for i in all:
    #     mylist.append({
    #         'name':i.name,
    #         'surname':i.surname,
    #         'thirdname':i.thirdname
    #     })
    return JsonResponse(mylist.data, safe=False)
    


def detail(request, myid):
    # each = get_object_or_404(location, id=myid)
    each = location.objects.filter(id=myid)
    # data={'City name':each.city, 'Country name':each.country}
    fornow=locationSerializer(each, many=True)
    return JsonResponse(fornow.data, safe=False)
