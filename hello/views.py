from django.shortcuts import render,HttpResponse
def home(request):
    return render(request, "index.html")
def registration(request):
    return HttpResponse("Registration")
def login(request):
    return HttpResponse("Longin")
def profile(request):
    return HttpResponse("Profile")
def notifications(request):
    return HttpResponse("Notifications")
def scoreboard(request):
    return HttpResponse("Scoreboard")
def challenges(request):
    return HttpResponse("Challenges")
def contests(request):
    return HttpResponse("Contests")
def settings(request):
    return HttpResponse("Settings")
