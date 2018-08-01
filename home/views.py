from django.shortcuts import render, redirect
from django.contrib.auth import logout

from django.views.generic.base import TemplateView
from django.views.generic.base import View
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')


def my_logout(request):
    logout(request)
    return redirect('home')


class HomePageView(TemplateView):

    template_name = "home2.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['home3_var'] = 'minha var em home3'
        return context


class MyView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, World GET!')

    def post(self, request, *args, **kwargs):
        return HttpResponse('Hello, World POST!')


