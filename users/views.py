from django.views.generic import View,TemplateView,FormView
from .forms import RegisterForm
from django.shortcuts import redirect,render
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.mixins import LoginRequiredMixin


class LoginView(View):
    http_method_names = ["get","post"]

    def get(self,request):
        return render(request,"account/login.html")

    def post(self,request):
        email    = request.POST.get("email")
        password = request.POST.get("password")
        user     = authenticate(username=email, password=password)

        if user is None:
            messages.error(request, _("Invalid login information."))
            return redirect("url_login")
        login(request, user)

        messages.success(request,_("You have successfully logged in."))
        return redirect("url_homepage")

class LogoutView(LoginRequiredMixin,View):
    http_method_names = ["get"]
    def get(self,request):
        logout(request)
        messages.success(request,_("You have successfully logged out."))
        return redirect("url_homepage")


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = "account/register.html"

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("url_homepage")


class DashboardView(LoginRequiredMixin,TemplateView):
    template_name = "account/dashboard.html"



