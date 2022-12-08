from django.urls import path
from . import views

app_name = "polls"

urlpatterns = [
    path("", views.indexview.as_view(), name="index"),
    path("<int:pk>", views.detailview.as_view(), name="detail"),
    path("<int:pk>/results/", views.resultview.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote")
]