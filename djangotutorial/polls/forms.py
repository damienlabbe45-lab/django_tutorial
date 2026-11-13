from django import forms
from django.utils import timezone
from .models import Question, Choice

class QuestionForm(forms.ModelForm):
    # Champs optionnels pour les choix
    choice1 = forms.CharField(label="Choix 1", required=True)
    choice2 = forms.CharField(label="Choix 2", required=True)
    choice3 = forms.CharField(label="Choix 3", required=False)
    choice4 = forms.CharField(label="Choix 4", required=False)
    choice5 = forms.CharField(label="Choix 5", required=False)

    class Meta:
        model = Question
        fields = ["question_text", "pub_date"]
        labels = {
            "question_text": "Intitulé de la question",
            "pub_date": "Date et heure de publication",
        }
        widgets = {
            # Génère un input HTML5 <input type="datetime-local">
            "pub_date": forms.DateTimeInput(
                attrs={"type": "datetime-local"},
                format="%Y-%m-%dT%H:%M"
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Valeur par défaut : la date et l'heure actuelles
        if not self.instance.pk and not self.initial.get("pub_date"):
            self.initial["pub_date"] = timezone.now().strftime("%Y-%m-%dT%H:%M")

    def save(self, commit=True):
        # 1. Sauvegarde de la question avec la pub_date saisie (ou actuelle)
        question = super().save(commit=commit)
        
        # 2. Création explicite des choix
        for i in range(1, 6):
            choice_text = self.cleaned_data.get(f"choice{i}")
            if choice_text and choice_text.strip():
                Choice.objects.create(
                    question=question,
                    choice_text=choice_text.strip(),
                    votes=0
                )
        return question