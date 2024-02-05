import datetime
from django.core.validators import RegexValidator
from django.db import models


# Create your models here.
class Portfolio(models.Model):
    name = models.CharField(max_length=50, unique=True)
    position = models.PositiveSmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)
    slug = models.CharField(max_length=50, unique=True, db_index=True)
    photo = models.ImageField(upload_to='portfolioes/')
    descr = models.TextField(max_length=500, default='')
    date = models.TextField(max_length=50, default=datetime.datetime.now())

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('position',)

class About(models.Model):
    name = models.CharField(max_length=50, unique=True)
    position = models.PositiveSmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='about/')
    descr = models.TextField(max_length=2000)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('position',)
class Services(models.Model):
    name = models.CharField(max_length=50, unique=True)
    position = models.PositiveSmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)
    icon = models.ImageField(upload_to='icon/')
    descr = models.TextField(max_length=500)

    class Meta:
        ordering = ('position',)

class Team(models.Model):
    name = models.CharField(max_length=50, unique=True)
    position = models.PositiveSmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)
    facebook_link = models.URLField(default='', blank=True)
    instagram_link = models.URLField(default='', blank=True)
    twitter_link = models.URLField(default='', blank=True)
    job = models.TextField(max_length=50)
    photo = models.ImageField(upload_to='team/')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('position',)

class Partners(models.Model):
    photo = models.ImageField(upload_to='partner/')
    url = models.URLField(default='', blank=True)



class Reservation(models.Model):

    name = models.CharField(max_length=70)
    email = models.EmailField()
    phone_regex = RegexValidator(
        regex=r'[0-9]{4,10}$',
        message="+38(0xx)xxxxxxx"
    )
    phone = models.CharField(validators=[phone_regex], max_length=20)
    message = models.TextField(max_length=300)

    is_proctssed = models.BooleanField(default=False)
    date_in = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_in',)