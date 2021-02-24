from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import AmarakuModel
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError


# Create your views here.

class TodoList(ListView):
    template_name = 'list.html'
    model = AmarakuModel

# サインイン機能
def signupfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username,'', password)
            return render(request, 'signup.html', {'text': '登録しました'})
        except IntegrityError:
            return render(request, 'signup.html', {'error': 'このユーザーネームはすでに使われています．'})

    return render(request, 'signup.html', {})

# ログイン
def loginfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('list')
        else:
            # Return an 'invalid login' error message.
            return render(request, 'login.html', {'context': 'ログインできませんでした．'})

    return render(request, 'login.html', {})

# ログアウト
def logoutfunc(request):
    logout(request)
    # Redirect to a success page.
    return redirect('login')