from django.shortcuts import render, get_object_or_404
from .models import fullname, location
from django.http import JsonResponse
from .serializer import fullnameSerializer, locationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

# def all(request):
#     all=fullname.objects.all()
#     mylist =fullnameSerializer(all, many=True)
#     # for i in all:
#     #     mylist.append({
#     #         'name':i.name,
#     #         'surname':i.surname,
#     #         'thirdname':i.thirdname
#     #     })
#     return JsonResponse(mylist.data, safe=False)

class getfullname(APIView):
    def get(self, request):
        bir = fullname.objects.all()
        srr=fullnameSerializer(bir, many=True)
        return Response(srr.data)

    


def detail(request, myid):
    # each = get_object_or_404(location, id=myid)
    each = location.objects.filter(id=myid)
    # data={'City name':each.city, 'Country name':each.country}
    fornow=locationSerializer(each, many=True)
    return JsonResponse(fornow.data, safe=False)

class postfullname(APIView):
    def post(self, request):
        main_body=request.data
        sss = fullnameSerializer(data=main_body)
        if sss.is_valid():
            sss.save()
            return Response(sss.data)
        return Response(sss.errors)

