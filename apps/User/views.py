# _*_ encoding:utf-8  _*_
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views.generic import View

from User.forms import LoginForm


class LoginView(View):
    def get(self, request):
        return render(request, "login.html", {})
    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get("username", "")
            pass_word = request.POST.get("password", "")
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                    return render(request, "200.html",{})
            else:
                return render(request, "404.html", {})
        else:
            return render(request, "404.html", {})
