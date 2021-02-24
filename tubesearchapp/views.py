from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import AmarakuModel
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.contrib.auth.models import User


# Create your views here.

class AmarakuList(ListView):
    template_name = 'list.html'
    model = AmarakuModel

class Create(CreateView):
    template_name = 'create.html'
    model = AmarakuModel
    fields = ('title', 'memo', 'url_ama', 'url_raku')
    success_url = reverse_lazy('list')

class Detail(DetailView):
    template_name = 'detail.html'
    model = AmarakuModel

class Delete(DeleteView):
    template_name = 'delete.html'
    model = AmarakuModel
    success_url = reverse_lazy('list')

class Update(UpdateView):
    template_name = 'update.html'
    model = AmarakuModel
    fields = ('title', 'memo', 'url_ama', 'url_raku')
    success_url = reverse_lazy('list')


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