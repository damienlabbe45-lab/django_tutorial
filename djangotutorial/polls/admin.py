from django.contrib import admin

from .models import Question, Choice




class QuestionAdmin(admin.ModelAdmin):
    ordering = ["pub_date", "question_text"]
    search_fields = ["question_text"]
    list_display = ["question_text", "pub_date", "id"]
    list_filter = ["question_text", "pub_date", "id"]


class ChoiceAdmin(admin.ModelAdmin):
    search_fields = ["choice_text"]
    ordering = ["question_id", "choice_text"]
    list_display = ["question_id", "choice_text", "votes", "id"]
    list_filter = ["question_id", "choice_text", "votes", "id"]
    


admin.site.register(Question, QuestionAdmin)

admin.site.register(Choice, ChoiceAdmin)