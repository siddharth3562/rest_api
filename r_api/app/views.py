from django.shortcuts import render
from .models import *
from .serializers import *
from django.http import JsonResponse,HttpResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.

def sample_fun(req):
    d=Api_user.objects.all()
    s=sample(d,many=True)
    return JsonResponse(s.data,safe=False)

@csrf_exempt
def mode_view(req):
    if req.method=='GET':
        d= Api_user.objects.all()
        s=mdl_serializer(d,many=True)
        return JsonResponse(s.data,safe=False)
    elif req.method=='POST':
        d=JSONParser().parse(req)
        s=mdl_serializer(data=d)
        if s.is_valid():
            s.save()
            return JsonResponse(s.data)
        else:
            return JsonResponse(s.errors)
        
@csrf_exempt
def update_view(req,id):
    try:
        demo=Api_user.objects.get(pk=id)
    except:
        return HttpResponse('invalid id')
    if req.method=='GET':
        s=mdl_serializer(demo)
        return JsonResponse(s.data,safe=False)
    elif req.method=='PUT':
        d=JSONParser().parse(req)
        s=mdl_serializer(demo,data=d)
        if s.is_valid():
            s.save()
            return JsonResponse(s.data)
        else:
            return JsonResponse(s.errors)
    elif req.method=='DELETE':
        demo.delete()
        return HttpResponse('deleted')
    
@api_view(['GET','POST'])
def fun1(req):
    if req.method=='GET':
        d=Api_user.objects.all()
        s=mdl_serializer(d,many=True)
        return Response(s.data)
    elif req.method=='POST':
        s=mdl_serializer(data=req.data)
        if s.is_valid():
            s.save()
            return JsonResponse(s.data,status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(s.data,status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET','PUT','DELETE'])
def fun2(req,id):
    try:
        demo=Api_user.objects.get(pk=id)
    except:
        return HttpResponse('invalid id')
    if req.method=='GET':
        s=mdl_serializer(demo)
        return Response(s.data)
    elif req.method=='PUT':
        s=mdl_serializer(demo,data=req.data)
        if s.is_valid():
            s.save()
            return JsonResponse(s.data,status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(s.errors,status=status.HTTP_400_BAD_REQUEST)
    elif req.method=='DELETE':
        demo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        