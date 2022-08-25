from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import *

#
# admin.site.register(Bolim)
# admin.site.register(Mavzu)
# admin.site.register(Dars)
# admin.site.register(Yangilik)
admin.site.register(Natija)
admin.site.register(Test)
admin.site.register(Variant)


@admin.register(Bolim)
class BolimAdmin(TranslationAdmin):
    list_display = ("nom",)
    search_fields = ('nom',)

@admin.register(Mavzu)
class MavzuAdmin(TranslationAdmin):
    list_display = ("nom",)

@admin.register(Dars)
class DarsAdmin(TranslationAdmin):
    list_display = ("nom", "matn")

@admin.register(Yangilik)
class YangilikAdmin(TranslationAdmin):
    list_display = ("nom", "matn")