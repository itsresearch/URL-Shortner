from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect

from .models import ShortURL
from .forms import RegisterForm, ShortURLForm
from .utils import generate_short_code


def register(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dashboard")
    else:
        form = RegisterForm()
    return render(request, "urlshortner/register.html", {"form": form})


class CustomLoginView(LoginView):
    template_name = "urlshortner/login.html"


class CustomLogoutView(LogoutView):
    next_page = "login"


@login_required
def dashboard(request):
    urls = ShortURL.objects.filter(user=request.user)
    return render(request, "urlshortner/dashboard.html", {"urls": urls})


@login_required
def create_short_url(request):
    if request.method == "POST":
        form = ShortURLForm(request.POST)
        if form.is_valid():
            ShortURL.objects.create(
                user=request.user,
                original_url=form.cleaned_data["original_url"],
                short_code=generate_short_code(ShortURL),
            )
            return redirect("dashboard")
    else:
        form = ShortURLForm()
    return render(request, "urlshortner/create.html", {"form": form})


def redirect_url(request, code):
    try:
        short_url = ShortURL.objects.get(short_code=code)
        short_url.clicks += 1
        short_url.save()
        return HttpResponseRedirect(short_url.original_url)
    except:
        return redirect("dashboard")


@login_required
def edit_short_url(request, code):
    try:
        short_url = ShortURL.objects.get(short_code=code, user=request.user)
    except:
        return redirect("dashboard")

    if request.method == "POST":
        form = ShortURLForm(request.POST)
        if form.is_valid():
            short_url.original_url = form.cleaned_data["original_url"]
            short_url.save()
            return redirect("dashboard")
    else:
        form = ShortURLForm(initial={"original_url": short_url.original_url})
    return render(
        request, "urlshortner/edit.html", {"form": form, "short_url": short_url}
    )


@login_required
def delete_short_url(request, code):
    try:
        short_url = ShortURL.objects.get(short_code=code, user=request.user)
    except:
        return redirect("dashboard")

    if request.method == "POST":
        short_url.delete()
        return redirect("dashboard")
    return render(request, "urlshortner/delete_confirm.html", {"short_url": short_url})
