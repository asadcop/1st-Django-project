from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('registration/',views.registration),
    path('login/',views.login),
    path('profile/',views.profile),
    path('notifications',views.notifications),
    path('scoreboard/',views.scoreboard),
    path('challenges/',views.challenges),
    path('contests/',views.contests),
    path('settings/',views.settings),

]
