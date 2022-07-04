from django.db import models
from django.contrib.auth.models import User

class User_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile') #Se generó un vínculo entre la clase User_profile y la clase User
    phone = models.CharField(max_length=20)
    image = models.ImageField(upload_to='profile_image', default='') #asigna una foto al perfil de usuario un "avatar" clase 24
    address = models.CharField(max_length=30,  default='')
    dni = models.CharField(max_length=30,  default='',unique=True )
    nombre = models.CharField(max_length=30, blank=True)
    apellido = models.CharField(max_length=30, blank=True)
    mail = models.EmailField(blank=True)
    is_active = models.BooleanField()
    def __str__(self):
        return f'{self.user}  {self.user.id}  {self.user.first_name}'
    class Meta:
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'



# información:  whats-the-difference-between-django-onetoonefield-and-foreignkey
# https://stackoverflow.com/questions/5870537/whats-the-difference-between-django-onetoonefield-and-foreignkey    

# what-is-the-difference-between-null-true-and-blank-true-in-django:  
# https://stackoverflow.com/questions/8609192/what-is-the-difference-between-null-true-and-blank-true-in-django
