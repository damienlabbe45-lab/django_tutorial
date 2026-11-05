from django.contrib import admin

from .models import Question, Choice


class ChoiceAdmin(admin.ModelAdmin):
    search_fields = ["choice_text"]
    ordering = ["question_id", "choice_text"]
    list_display = ["question_id", "choice_text", "votes", "id", "was_published_recently"]
    list_filter = ["question_id", "choice_text", "votes", "id"]


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    ordering = ["pub_date", "question_text"]
    search_fields = ["question_text"]
    list_display = ["question_text", "pub_date", "id"]
    list_filter = ["question_text", "pub_date", "id"]
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)

admin.site.register(Choice, ChoiceAdmin)