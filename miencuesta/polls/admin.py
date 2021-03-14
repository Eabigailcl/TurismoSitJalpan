

from django.contrib import admin

from .models import Question, Choice, Sectores, Encuesta, AplEncuestaCF, AplEncuestaT, AplEncuestaR, AplEncuestaH
from django.forms import Textarea
from django.db import models


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionInline(admin.TabularInline):
    model = Question

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class SectoresAdmin(admin.ModelAdmin):
    list_display=("Nombre", "Descripcion")



admin.site.register(Sectores, SectoresAdmin)


class EncuestaAdmin(admin.ModelAdmin):
    list_display=("sectores", "fecha")
    inlines = [QuestionInline]
    inlines = [ChoiceInline]


admin.site.register(Encuesta, EncuestaAdmin)



# Q Y class

class ChoiceInline(admin.StackedInline):
    model = Choice
