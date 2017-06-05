from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from polls.models import Question, Choice

# Create your views here.

"""
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

"""


class Index(generic.ListView):
    model = Question
    template_name = 'polls/index.html'


"""
def detail(request, question_id):
    q = Question.objects.get(id=question_id)
    context = {'question': q}
    return render(request, 'polls/view.html', context)
"""


class detail(generic.DetailView):
    model = Question
    pk_url_kwarg = 'question_id'
    template_name = 'polls/view.html'


def results(request, question_id):
    q = Question.objects.get(id=question_id)

    maxv = 0
    mvote = None
    for i in q.choice_set.all():
        if i.votes > maxv:
            maxv = i.votes
            mvote = i

    context = {'question': q, 'mvote': mvote}
    return render(request, 'polls/result.html', context)


def vote(request, question_id):
    if request.method == 'POST':
        question = get_object_or_404(Question, pk=question_id)
        try:
            selected_choice = question.choice_set.get(pk=request.POST['choice'])
        except (KeyError, Choice.DoesNotExist):
            return render(request, 'polls/vote.html', {
                'question': question,
                'error_message': "You didn't select a choice.",
            })
        else:
            selected_choice.votes += 1
            selected_choice.save()
            # Always return an HttpResponseRedirect after successfully dealing
            # with POST data. This prevents data from being posted twice if a
            # user hits the Back button.
            return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    else:
        q = Question.objects.get(id=question_id)
        context = {'question': q}
        return render(request, 'polls/vote.html', context)
