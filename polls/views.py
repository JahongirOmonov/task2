from django.shortcuts import render, get_object_or_404
from .models import fullname, location
from django.http import JsonResponse

# Create your views here.

def all(request):
    all=fullname.objects.all()
    mylist =[]
    for i in all:
        mylist.append({
            'name':i.name,
            'surname':i.surname,
            'thirdname':i.thirdname
        })
    return JsonResponse(mylist, safe=False)
    


def detail(request, myid):
    each = location.objects.get(id=myid)
    each = get_object_or_404(location, id=myid)
    data={'City name':each.city, 'Country name':each.country}
    return JsonResponse(data)
