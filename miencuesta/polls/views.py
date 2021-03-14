from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
#from django.core.urlresolvers import reverse
from django.urls import reverse
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
#from rest_framework.renderers import JSONRenderer
#from rest_framework.parsers import JSONParser
import datetime
from django.utils import timezone
# from .serializers import QuestionSerializer
from .models import Choice, Question, Sectores, Encuesta




class IndexView(generic.ListView):         
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-id')


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'




# Crear encuestas ####################################################################################################################################################################################
"""
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
"""
def createPoll(request):
	return render(request, 'polls/create_poll.html')

def newPoll(request):
	if request.method == "POST":
		q = Question(question_text=request.POST['name'], pub_date=timezone.now())
		q.save()

		c = Choice(question = q, choice_text = request.POST['option1'], votes=request.POST['votes1'])
		c.save()

		c = Choice(question = q, choice_text = request.POST['option2'], votes=request.POST['votes2'])
		c.save()

		c = Choice(question = q, choice_text = request.POST['option3'], votes=request.POST['votes3'])
		c.save()

	return HttpResponse("Encuesta Creada")

def deletePoll(request):
	poll_list = Question.objects.order_by('-pub_date')
	context = { 'poll_list' : poll_list }
	return render(request, 'polls/delete_poll.html',context)

def deleteOnePoll(request):

	try:
	    q = Question.objects.get(pk=request.POST['poll'])
	except (KeyError, Question.DoesNotExist):
		return render(request, 'polls/delete_poll.html', {
			'error_message': "Seleciona pregunta.",})
	else:
		q.delete()
		return HttpResponse("Pregunta eliminada")

# fin de crear encuesta ####################################################################################################################################################################################

# votar encuesta en pregunta################################################################################################################################################################################

def guardar(request,question_id):
    #  obtienes la pregunta
    p = get_object_or_404(Question, pk=question_id)
    try:  #  en el orden en que las quieras mostrar
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return HttpResponse("No has seleccionado ninguna opcion")
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponse("¡voto registrado, gracias por participar!")


def GuardarFecha(request,encuesta_id):
    p = get_object_or_404(Encuesta, pk=encuesta_id)
    try:
        Enviar_fecha = p.timezone.now(pk=request.POST['encuesta'])
    except (KeyError, Choice.DoesNotExist):
        return HttpResponse("No has llenado todas las preguntas")
    else:
        Enviar_fecha.save()
        return HttpResponseRedirect(reverse('polls:sectores'))



"""
def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "No has seleccionado ninguna opcion.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "Pregunta Contestada.",
            })
    """
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
#        return HttpResponseRedirect(reverse('detail', args=(p.id,)))


# fin  ######################################################################################################################################################################################################

#  funcion para mostrar los sectores en una lista en vista
def list_sectoreslist(request):
    lists = Sectores.objects.order_by('-id')  #  consulta en python a la base de datos
    context = {'lists': lists}  #  generacion de un contexto
    return render(request, 'polls/sectores.html', context)  #  se retorna un resultado en un html y se llama el contexto

def detail_sectoreslist(request, id):  #  se crea una vista detalle para separar el contenido de cada sector
    model = Question
    object = get_object_or_404(Sectores, pk=id)  #  se declara el error 404 y los parametros
    latest_question_list = Question.objects.filter(encuesta__sectores_id = id)  #  consulta en python a la base de datos
    context = {'list': object, 'latest_question_list':latest_question_list}  #  se genera el contexto
    return render(request, 'polls/detail_sectores.html', context)  #  se retorna un resultado en un html y se llama el contexto
