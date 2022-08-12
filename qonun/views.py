from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from .models import *

class Bolim(View):
    def get(self, request):
        return render(request, 'index.html')

    def put(self, request, pk):
        data = {
            'bolimlar': Bolim.objects.filter(id=pk)
        }
        return render(request, 'index.html', data)

class News(View):
    def get(self, request):
        return render(request, 'news1.html')

class Yangiliklar(View):
    def get(self, request):
        data = {
            'yangilik': Yangilik.objects.all()
        }
        return render(request, 'yangiliklar.html', data)

class Biz_haqimizda(View):
    def get(self, request):
        return render(request, 'biz-haqimizda.html')

class Foydalanish(View):
    def get(self, request):
        return render(request, 'foydalanish.html')

class Mehnat(View):
    def get(self, request):
        return render(request, 'mehnat-m.html')

class Qabul(View):
    def get(self, request):
        return render(request, 'qabul.html')

class Login(View):
    def post(self, request):
        l = request.POST.get('l'),
        p = request.POST.get('p')
        user =authenticate(username=l, password=p)
        if user is None:
            return redirect('/login/')
        else:
            login(request, user)

