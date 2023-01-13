from django.shortcuts import render
from .models import Msg


def home(req):
    return render(req,"chatapp/login.html")

def chat(req):
    M = Msg.objects.all()
    return render(req,"chatapp/chat.html",{'msg':M})
