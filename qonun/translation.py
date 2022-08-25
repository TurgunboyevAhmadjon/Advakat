from modeltranslation.translator import TranslationOptions, register
from .models import *

@register(Bolim)
class BolimTranslationOptions(TranslationOptions):
    fields = ("nom",)

@register(Mavzu)
class MavzuTranslationOptions(TranslationOptions):
    fields = ("nom",)

@register(Dars)
class DarsTranslationOptions(TranslationOptions):
    fields = ("nom", "matn",)

@register(Yangilik)
class YangilikTranslationOptions(TranslationOptions):
    fields = ("nom", "matn",)