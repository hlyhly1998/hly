import uuid

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from cb.forms import UserForm
from cb.models import Wheel


def base(request):
    return render(request, 'base.html')


def home(request):
    wheels = Wheel.objects.all()
    data = {
        'wheels':wheels,
    }

    return render(request, 'home.html', context=data)

# 關於表單之注冊界面
def new_form(request):
    if request.method != 'POST':
        form = UserForm()

    else:
        form = UserForm(request.POST)
        if form.is_valid():
            form.token = str(uuid.uuid5(uuid.uuid4(), 'register'))
            form.save()
            request.session['token'] = form.token
            return HttpResponseRedirect(reverse('cb:home'))
    data = {'form':form}
    return render(request, 'regirest.html', context=data)

