

import datetime

from django.db import models
from django.utils import timezone


# Create your models here.

class Sectores(models.Model):
	Nombre = models.CharField(max_length=100)
	Descripcion = models.TextField()


	def __str__(self):
		return self.Nombre

class Encuesta(models.Model):
	sectores = models.ForeignKey(Sectores, on_delete=models.CASCADE)
	fecha = models.DateField(auto_now_add=True)


class Question(models.Model):
	encuesta = models.ForeignKey(Encuesta, on_delete=models.CASCADE)
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField()

	def __str__(self):              # __unicode__ on Python 2
		return self.question_text

	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <= now

	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
	encuesta = models.ForeignKey(Encuesta, on_delete=models.CASCADE)
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __str__(self):              # __unicode__ on Python 2
		return self.choice_text

class AplEncuestaCF(models.Model):
	encuesta = models.ForeignKey(Encuesta, on_delete=models.CASCADE)
	fecha = models.DateField(auto_now_add=True)

class AplEncuestaR(models.Model):
	encuesta = models.ForeignKey(Encuesta, on_delete=models.CASCADE)
	fecha = models.DateField(auto_now_add=True)

class AplEncuestaT(models.Model):
	encuesta = models.ForeignKey(Encuesta, on_delete=models.CASCADE)
	fecha = models.DateField(auto_now_add=True)

class AplEncuestaH(models.Model):
	encuesta = models.ForeignKey(Encuesta, on_delete=models.CASCADE)
	fecha = models.DateField(auto_now_add=True)
