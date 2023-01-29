from django.urls import path
from . import views

urlpatterns = [
    path("", views.upload_file, name="upload"),
    path("success/", views.successViews.as_view()),
    path("success/<nome_l>/", views.successDetailsViews.as_view()),
]