from django.shortcuts import render
from .forms import SearchForm,  RegisterForm, LoginForm


def index(request):
    """首页"""
    context = dict(
        searchForm=SearchForm
    )
    return render(request, 'book/index.htm', context)


def register(request):
    register_form = RegisterForm
    state = None

    context = dict(
        state=state,
        registerForm=register_form
    )
    return render(request, 'book/register.htm', context)


def login(request):
    login_form = LoginForm
    state = None

    context = dict(
        state=state,
        loginForm=login_form
    )
    return render(request, 'book/login.htm', context)


def search(request):
    pass

