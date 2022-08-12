from django.contrib import admin
from django.urls import path
from qonun.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('advice/', Bolim.as_view()),
    path('bolim/<int:pk>/', Bolim.as_view()),
    path('news1/', News.as_view()),
    path('news/', Yangiliklar.as_view()),
    path('about/', Biz_haqimizda.as_view()),
    path('foydalanish/', Foydalanish.as_view()),
    path('mehnat/', Mehnat.as_view()),
    path('qabul/', Qabul.as_view()),
]
