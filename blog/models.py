#-*-coding: utf-8-*
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profil(models.Model):
    user = models.OneToOneField(User)

    def __unicode__(self):
        return "Profil: {0}".format(self.user.username)



class Categorie(models.Model):
    nom_categorie = models.CharField(max_length=20)

    def __unicode__(self):
        return u"%s" % self.nom_categorie



class Article(models.Model):
    titre = models.CharField(max_length=100)
    auteur = models.CharField(max_length=42)
    contenu = models.TextField(null=True)
    source = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de publication")
    categorie = models.ForeignKey(Categorie)

    def __unicode__(self):
        return u"%s" % self.titre

