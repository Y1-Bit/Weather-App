from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .forms import RegisterForm, LocationSearchForm
from .models import Location
from .utils import search_locations, get_weather


# Create your views here.
def home(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        locations = Location.objects.filter(user=request.user)
        weather_data = [get_weather(loc.latitude, loc.longitude) for loc in locations]
        context = {"locations": zip(locations, weather_data)}
        return render(request, "home.html", context)
    return render(request, "home.html")



def register(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})


@login_required
def weather_search_view(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = LocationSearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data["query"]
            weather_data = search_locations(query)
            context = {"weather": weather_data, "form": form}
            return render(request, "weather_search.html", context)

    else:
        form = LocationSearchForm()
    return render(request, "weather_search.html", {"form": form})