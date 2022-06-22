from django.db import models

# Create your models here.




class Customize(models.Model):
    title1 = models.CharField(max_length=200, blank=True, null=True)
    title2 = models.CharField(max_length=200, blank=True, null=True)
    text_footer = models.CharField(max_length=200, blank=True, null=True)
    logo = models.ImageField(upload_to='logo', default='') #asigna una foto al perfil de usuario un "avatar" clase 24
    def __str__(self):
        return f"Titulo1: {self.title1} - Titulo2: {self.title2} - Texto footer: {self.text_footer} - Logo: {self.logo.url}"