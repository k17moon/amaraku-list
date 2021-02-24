"""todoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from .views import signupfunc, loginfunc, logoutfunc
    # TodoList, TodoDetail, TodoCreate, TodoDelete, TodoUpdate, signupfunc, loginfunc, logoutfunc

urlpatterns = [
    path('list/', TodoList.as_view(), name='list'),
    # ログイン機能を追加
    path('signup/', signupfunc, name='signup'),
    path('login/', loginfunc, name='login'),
    path('logout/', logoutfunc, name='logout'),

    # path('detail/<int:pk>/', TodoDetail.as_view(), name='detail'),
    # path('create/', TodoCreate.as_view(), name='create'),
    # path('delete/<int:pk>/', TodoDelete.as_view(), name='delete'),
    # path('update/<int:pk>/', TodoUpdate.as_view(), name='update'),


]
