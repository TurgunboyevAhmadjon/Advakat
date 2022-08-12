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
    mavzu = models.ForeignKey(Mavzu, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

class Yangilik(models.Model):
    nom = models.CharField(max_length=100)
    rasm = models.FileField(blank=True)
    sana = models.DateTimeField(auto_now_add=True)
    matn = models.CharField(max_length=900, blank=True)
    oqildi = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.nom} {self.rasm} {self.sana}{self.matn} {self.oqildi}"