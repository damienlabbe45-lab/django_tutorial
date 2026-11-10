from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views

app_name = "polls"
urlpatterns = [
    path("logout/", LogoutView.as_view(next_page="polls:index"), name="logout"),
    path("connection/", LoginView.as_view(template_name = "polls/connection.html", next_page = ""), name = "connection"),
    path("new_poll/", views.create_question, name="create"),
    path("statistics/", views.StatisticsView.as_view(), name = "statistics"),
    path("<int:pk>/frequency/", views.FrequencyView.as_view(), name="frequency"),
    path("all/", views.AllView.as_view(), name="all"),
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]