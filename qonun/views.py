from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from .models import Bolim, Yangilik, Mavzu, Dars, Variant


class Bolimlar(View):
    def get(self, request):
        data = {
            'bolimlar': Bolim.objects.all(),
        }
        return render(request, 'index.html', data)

class BolimView(View):
    def get(self, request, pk):
        b = Bolim.objects.get(id=pk)
        data = {
            'bolim': b,
            'bolimlar': Bolim.objects.filter(id=pk),
            'mavzular': Mavzu.objects.filter(bolim=b),
            'darslar': Dars.objects.all()
        }
        return render(request, 'mehnat-m.html', data)

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

class MehnatView(View):
    def get(self, request):
        return render(request, 'mehnat-m.html')

class MehnatId(View):
    def get(self, request, pk):
        data = {
            'bolimlar': Bolim.objects.filter(id=pk),
        }
        return render(request, 'mehnat-m.html', data)

class Qabul(View):
    def get(self, request):
        data = {
            'bolimlar': Bolim.objects.all(),
        }
        return render(request, 'qabul.html', data)

class Login(View):
    def post(self, request):
        l = request.POST.get('l'),
        p = request.POST.get('p')
        user =authenticate(username=l, password=p)
        if user is None:
            return redirect('/login/')
        else:
            login(request, user)

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("home")

class NatijaView(View):
    def post(self, request, pk):
        d = Dars.objects.get(id=pk)
        testlar_soni = d.dars_testlari.all().count()
        natijalar = 0
        for test in d.dars_testlari.all():
            print(request.POST.get(test.savol))
            tanlangan_var = Variant.objects.get(id=request.POST.get(test.savol))
            if tanlangan_var.togri == True:
                natijalar = natijalar + 1
        print(natijalar, testlar_soni, natijalar* 100/testlar_soni)
        nat = Natija.onjects.filter(user=request.user, dars=d)
        if nat and not nat.foiz >= 70:
            NatijaView.objects.create(
                user = request.user,
                dars = d,
                togrilar_soni = natijalar,
                testlar_soni = testlar_soni,
                foiz = natijalar*100/testlar_soni
            )
        return redirect("dars", pk)




from urllib.parse import urlparse
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls.base import resolve, reverse
from django.urls.exceptions import Resolver404
from django.utils import translation


def set_language(request, language):
    for lang, _ in settings.LANGUAGES:
        translation.activate(lang)
        try:
            view = resolve(urlparse(request.META.get("HTTP_REFERER")).path)
        except Resolver404:
            view = None
        if view:
            break
    if view:
        translation.activate(language)
        next_url = reverse(view.url_name, args=view.args, kwargs=view.kwargs)
        response = HttpResponseRedirect(next_url)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    else:
        response = HttpResponseRedirect("/")
    return response

