from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.views import generic

from polls.models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class _QuestionDetailView(generic.DetailView):
    def get_queryset(self):
        """Excludes any questions that are not published yet."""
        return Question.objects.filter(pub_date__lte=timezone.now())


class DetailView(_QuestionDetailView):
    template_name = 'polls/detail.html'


class ResultsView(_QuestionDetailView):
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
