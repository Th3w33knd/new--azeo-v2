from django.shortcuts import render, redirect
from . import forms
from .models import Team


# Homepage
def homepage(request):
    return render(request, "webapp/home.html")


# Team
def team(request):
    team = Team.objects.all().order_by("role")
    return render(request, "webapp/team.html", {"team": team})


# Azeo ID Registration
def azeoid_register(request):
    if request.method == "POST":
        form = forms.AzeoidRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = forms.AzeoidRegistrationForm()
    return render(request, "webapp/register-azeoid.html", {"form": form})
