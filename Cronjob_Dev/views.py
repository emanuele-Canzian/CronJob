from pyexpat.errors import messages

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from passlib.hash import pbkdf2_sha256
from Cronjob_Dev.models import CronJob
from .forms import SignUpForm

# Create your views here.

from django.http import HttpResponse


def index(request):
    return render(request, 'Cronjob_Dev/index.html', {})


# login
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in.')
            return redirect('cron')
        else:
            messages.error(request, 'Incorrect Info')
            return redirect('login')
    else:
        return render(request, 'Cronjob_Dev/login_user.html', {})


def cron(request):
    return render(request, 'Cronjob_Dev/cron.html')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'u have been registet')
            return redirect('cron')

    else:
        form = SignUpForm()

    context = {'form': form}
    return render(request, 'Cronjob_Dev/register_user.html', context)


def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logout')
    return redirect('index')


def cron(request):
    if request.method == 'POST':
        tablefill = CronJob()
        title = request.POST.get('title')
        url = request.POST.get('url')

        auth = request.POST.get('auth')
        if auth == 'on':
            auth = True
        if auth is None:
            auth = False

        username = request.POST.get('username')

        password = request.POST.get('password')
        if password != '':
            enc_password = pbkdf2_sha256.encrypt(password, rounds="12000", salt_size=32)
        else:
            enc_password = ''

        if auth == 'on' and username == '' or password == '':
            messages.error(request, 'wen http aktiviert ist müssen sie einen benutzer und Passwort eingeben')
            return render(request, 'Cronjob_Dev/cron.html')

        auswahl = request.POST.get('ausführung')
        if auswahl == '1':
            minute = request.POST.get('mins')
            minute = tablefill.minute
        if auswahl == '2':
            hour = request.POST.get('hours')
            hour = tablefill.hour
            minute = request.POST.get('minutes')
            minute = tablefill.minute
        if auswahl == '3':
            day = request.POST.get('days')
            day = tablefill.dayOfMonth
            hour = request.POST.get('hour')
            hour = tablefill.hour
            minute = request.POST.get('minut')
            minute = tablefill.minute

        tablefill.title = title
        tablefill.url = url
        tablefill.username = username
        tablefill.password = password
        tablefill.auth = auth

        tablefill.save()

        return render(request, 'Cronjob_Dev/cron.html')
    else:
        return render(request, 'Cronjob_Dev/cron.html')
