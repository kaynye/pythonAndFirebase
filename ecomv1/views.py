from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User, Group
import firebase_admin
from firebase_admin import credentials,firestore
from django.conf import settings
import os
from django.contrib import messages  # import messages
import json
import requests
# firestore_db = firestore.client()

# cred = credentials.Certificate(os.path.join(settings.BASE_DIR, 'serviceAccountKey.json'))
# firebase_admin.initialize_app(cred)

# Create your views here.

from django.contrib.auth import login, authenticate, logout



def loginpage(request):
    print("jfeijij")
    return render(request,"ecomv1/loginpage.html", {})

def postsignIn(request):
    print("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
    email=request.POST.get('email')
    password=request.POST.get('pass')
    print(email)
    print(password)
    payload = json.dumps({
        "email": email,
        "password": password,
        "returnSecureToken": True
    })

    rest_api_url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword"
    FIREBASE_WEB_API_KEY="AIzaSyCAfLF30pl7hLCsjCihniOxomZ-eM_80bw"
    r = requests.post(rest_api_url,
                      params={"key": FIREBASE_WEB_API_KEY},
                      data=payload)
    print(r.json())
    if request.POST.get("email") and request.POST.get("pass"):
        user = authenticate(
            username=email, password=password
        )
        print(user)
        if user is not None:
            login(request, user)
            print(user)
            return redirect("django_app:loginpage")
        else:
            print("erreur ")
            messages.error(request, "Votre username et/ou mot de passes sont incorrect." )
            return render(request, "ecomv1/loginpage.html", {"erreur": True})



    # try:
    #     # if there is no error then signin the user with given email and password
    #         # = (email,pasw)
    # except:
    #     message="Invalid Credentials!!Please ChecK your Data"
    #     return render(request,"Login.html",{"message":message})
    # session_id=user['idToken']
    # request.session['uid']=str(session_id)
    return render(request,"Home.html",{"email":email})

    