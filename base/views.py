from django.shortcuts import render
from django.http import JsonResponse
from .models import Profile

# Create your views here.
def homepage(request):
    context = {

    }
    return render(request, "base/home.html", context)

def getprofiles(request):
    profiles = Profile.objects.all()
    return JsonResponse({"profiles":list(profiles.values())})

