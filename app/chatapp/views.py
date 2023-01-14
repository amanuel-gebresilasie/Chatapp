from django.shortcuts import render,HttpResponse,redirect
from .models import Msg
from django.views.decorators.csrf import csrf_exempt


def home(req):
    return render(req,"chatapp/login.html")

def chat(req):
    M = Msg.objects.all()
    return render(req,"chatapp/chat.html",{'msg':M})

@csrf_exempt
def save_msg(req):
    try:
       M = Msg(name=req.POST.get('name'),date=req.POST.get('date'),msg=req.POST.get('msg'))
       M.save()
       return HttpResponse("saved")
    except:
        return HttpResponse("not saved")
    return redirect("/")
