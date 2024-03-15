from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Profile

# Create your views here.
def homepage(request):
    context = {

    }
    return render(request, "base/home.html", context)

def getprofiles(request):
    profiles = Profile.objects.all()
    return JsonResponse({"profiles":list(profiles.values())})


def create(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        bio = request.POST['email']

        new_profile = Profile(name=name, email=email, bio=bio)
        new_profile.save()
        return HttpResponse("new profile created succesfully")

