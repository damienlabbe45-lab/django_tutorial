from typing import Any

from django.contrib.auth.decorators import login_required
from django.db.models import F, Sum
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import Choice, Question
from .forms import QuestionForm

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[
        :5
    ]

class AllView(IndexView):
    template_name = "polls/all.html"

    def get_queryset(self):
        """Return all published questions."""
        return Question.objects.order_by("-pub_date")


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(DetailView):
    template_name = "polls/results.html"

class FrequencyView(DetailView):
    template_name = "polls/frequency.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = Choice.objects.get(pk=request.POST["choice"], question=question)
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.pk,)))


class StatisticsView(generic.TemplateView):
    template_name = "polls/statistics.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["total_polls"] = Question.objects.count()
        context["total_choices"] = Choice.objects.count()
        context["total_votes"] = Choice.objects.aggregate(Sum('votes'))['votes__sum'] or 0
        context['avg_votes'] = context["total_votes"] / context["total_polls"] if context["total_polls"] > 0 else 0

        context['most_popular'] = Question.get_most_popular()

        context['least_popular'] = Question.get_least_popular()

        context["latest_question"] = Question.objects.order_by("-id").first()

        return context

@login_required(login_url="/")
def create_question(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("polls:index"))
    else:
        form = QuestionForm()
        
    return render(request, "polls/new_poll.html", {"form": form})
