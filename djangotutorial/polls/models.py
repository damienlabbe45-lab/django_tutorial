import datetime

from django.db import models
from django.utils import timezone
from django.db.models import Sum


class TextExcerptModel(models.Model):
    max_length=20

    class Meta:
        abstract = True

    def text_excerpt(self,text:str):
        return text[:self.max_length] + ('...' if len(text) > self.max_length else '')


class Question(TextExcerptModel):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.text_excerpt(self.question_text)

    def was_published_recently(self):
      #  return self.pub_date >= timezone.now() - datetime.timedelta(days=1) and self.pub_date <= timezone.now()
      return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    @property
    def age(self):
        return timezone.now() - self.pub_date

    def prepare_choices_context(self):
        choices = Choice.objects.filter(question=self)
        resultat = choices.aggregate(total=Sum('votes'))
        return (1 if resultat['total'] in [0, None] else resultat['total'], choices)
        

    def get_choices(self):
        total, choices = self.prepare_choices_context()
        return [(c.choice_text, c.votes, c.votes / total) for c in choices]


    def get_max_choice(self):
        total, choices = self.prepare_choices_context()
        max_choice = max(choices, key=lambda c: c.votes / total)
        return (max_choice.choice_text, max_choice.votes / total)

    @classmethod
    def get_most_popular(cls):
        return cls.objects.annotate(total_votes = Sum('choice__votes')).order_by('-total_votes').first()

    @classmethod
    def get_least_popular(cls):
        return cls.objects.annotate(total_votes = Sum('choice__votes')).order_by('total_votes').first()


class Choice(TextExcerptModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


    def __str__(self):
        return self.text_excerpt(self.choice_text)


