from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    email = models.CharField(max_length=200)
    nome = models.CharField(max_length=200)
    empresa = models.CharField(max_length=200, blank=True)
    cargo = models.CharField(max_length=200, blank=True)
    pais = models.CharField(max_length=200, blank=True)
    endereco = models.CharField(max_length=200, blank=True)
    celular = models.CharField(max_length=200, blank=True)
    sobre = models.CharField(max_length=10000, blank=True)
    twitter = models.CharField(max_length=200, blank=True)
    facebook = models.CharField(max_length=200, blank=True)
    instagram = models.CharField(max_length=200, blank=True)
    linkedin = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"Nome: {self.nome}, email: {self.email}, Administrador: {self.cargo}"


class UserActivity(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=1000)
    data = models.DateTimeField()
    tipo = models.CharField(max_length=200)
    obs = models.CharField(max_length=1000)
    link = models.CharField(max_length=1000)

    def __str__(self):
        return f"Usuario: {self.usuario}, descrição: {self.descricao}, data: {self.data}, tipo: {self.tipo}, obs: {self.obs}, link: {self.link}"



