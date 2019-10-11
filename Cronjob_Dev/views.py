from pyexpat.errors import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
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
            return redirect('index')
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
            return redirect('index')

    else:
        form = SignUpForm()

    context = {'form': form}
    return render(request, 'Cronjob_Dev/register_user.html', context)


def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logout')
    return redirect('index')

def screen(request):
    all_records = CronJob.objects.all
    return render(request, 'Cronjob_Dev/screen.html', {'all_records': all_records})





def index(request):

    if request.method == 'POST':
        tablefill = CronJob()
        title = request.POST.get('title')
        url = request.POST.get('url')

        auth = request.POST.get('auth')
        if auth == 'on':
            auth = True
            username = request.POST.get('username')
            password = request.POST.get('password')

            if password != '':
                enc_password = pbkdf2_sha256.encrypt(password, rounds="12000", salt_size=32)
            else:
                enc_password = ''
            if auth == 'on' and username == '' or password == '':
                messages.error(request, 'wen http aktiviert ist müssen sie einen benutzer und Passwort eingeben')
                return render(request, 'Cronjob_Dev/index.html')
        if auth is None:
            auth = False

        auswahl = request.POST.get('ausführung')
        username = request.POST.get('username')
        password = request.POST.get('password')
        if auswahl == 'firstbut':
            minute = request.POST.get('min1')

            tablefill.minute = minute
            tablefill.cronejob = minute + " *" + " *" + " *" + " *"

        if auswahl == 'secondbut':
            hour = request.POST.get('hour1')
            minute = request.POST.get('min2')
            tablefill.cronejob = minute + hour + " *" + " *" + " *"

        if auswahl == 'thirdbut':
            day = request.POST.get('day')
            hour = request.POST.get('hour2')
            minute = request.POST.get('min3')
            tablefill.cronejob = minute + hour + day + " *" + " *"



        tablefill.title = title
        tablefill.url = url
        tablefill.username = username
        tablefill.password = password
        tablefill.auth = auth
        tablefill.save()

        return render(request, 'Cronjob_Dev/index.html')
    else:
        return render(request, 'Cronjob_Dev/index.html')

