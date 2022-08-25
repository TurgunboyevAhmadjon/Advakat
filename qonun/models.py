from django.contrib.auth.models import User
from django.db import models

class Bolim(models.Model):
    nom = models.CharField(max_length=100)
    rasm = models.FileField(blank=True)

    def __str__(self):
        return self.nom


class Mavzu(models.Model):
    nom = models.CharField(max_length=100)
    bolim = models.ForeignKey(Bolim, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

class Dars(models.Model):
    nom = models.CharField(max_length=100)
    rasm = models.FileField(blank=True)
    matn = models.TextField(max_length=1000)
    oqildi = models.PositiveIntegerField()
    mavzu = models.ForeignKey(Mavzu, on_delete=models.CASCADE, related_name="mavzu_darslari")

    def __str__(self):
        return self.nom

class Yangilik(models.Model):
    nom = models.CharField(max_length=100)
    rasm = models.FileField(upload_to='rasmlar', null=True, blank=True)
    sana = models.DateTimeField(auto_now_add=True)
    matn = models.CharField(max_length=900, blank=True)
    oqildi = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.nom} {self.rasm} {self.sana}{self.matn} {self.oqildi}"

class Test(models.Model):
    savol = models.CharField(max_length=100)
    dars = models.ForeignKey(Dars, on_delete=models.CASCADE, related_name="dars_testlari")

    def __str__(self):
        return self.savol[:30]

class Variant(models.Model):
    variant_matn = models.CharField(max_length=1000)
    togri = models.BooleanField()
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name="test_variantlari")

    def __str__(self):
        return self.variant_matn[:30]

class Natija(models.Model):
    testlar_soni = models.PositiveIntegerField()
    togrilar_soni = models.PositiveIntegerField()
    foiz = models.CharField(max_length=100)
    dars = models.ForeignKey(Dars, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_natijalari")

    def __str__(self):
        return self.testlar_soni