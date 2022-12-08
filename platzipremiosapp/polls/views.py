from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse , HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice
from . import url
from django.views import generic

class indexview(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "lastest_question_list"
    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:5]

class detailview(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

class resultview(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

def vote(request,question_id):
    question = get_object_or_404(Question,pk=question_id)   
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html",{
            "question": question,
            "error_message": "no elegiste una respuesta"
        })
    else:
        selected_choice.votes +=1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question_id,)))






# Create your views here.
