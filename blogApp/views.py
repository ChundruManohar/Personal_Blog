from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from blogApp.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.
@csrf_exempt
def register_user(request):
    try:
        if request.method != "POST":
            return JsonResponse({
                "status": "error",
                "message": "Method Not Allowed"
            })
        data = json.loads(request.body)
        email = data.get('email')
        username = data.get('username') 
        password = data.get('password') 
        phone_num = data.get('phone_num')
        canCreateBlog=data.get('canCreateBlog')
        if email is None or username is None or password is None or phone_num is None:
            return JsonResponse({
                "status": "error",
                "message":"incomplete data"
            })
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            phone_num=phone_num,
            canCreateBlog = canCreateBlog
        )
        user.save()
        return JsonResponse({
             "status":"Success",
             "message":f"User {username} registered"
        })
    except Exception as e:
        return JsonResponse({
          "status": "error",
          "message":str(e)
        })

@csrf_exempt
def login_user(request):
    try:
        if request.method != "POST":
            return JsonResponse({
                "status": "error",
                "message": "Method Not Allowed"
            })
        data = json.loads(request.body)
        username = data.get('username')
        passwords = data.get('password')
        if username == None or passwords == None:
            return JsonResponse({
                "status": "error",
                "message":"incomplete data"
            })
        user = authenticate(request,username = username, password = passwords)
        if user is not None:
            reft = RefreshToken.for_user(user)
            return JsonResponse({
                "refreshToken":str(reft),
                "acessToken":str(reft.access_token),
            })      
    except Exception as e:
        return JsonResponse({
            "status": "Failed",
            "message":str(e),
        })
