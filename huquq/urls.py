from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path
from django.views.i18n import set_language
from qonun.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('advice/', Bolimlar.as_view(), name="home"),
    path('bolim/<int:pk>/', BolimView.as_view()),
    path('news1/', News.as_view()),
    path('yangiliklar/', Yangiliklar.as_view()),
    path('about/', Biz_haqimizda.as_view()),
    path('foydalanish/', Foydalanish.as_view()),
    path('mehnat/', MehnatView.as_view()),
    path('qabul/', Qabul.as_view()),
]

urlpatterns = [
    *i18n_patterns(*urlpatterns, prefix_default_language=False),
    path("set_language/<str:language>/", set_language, name="set-language"),
    ]
