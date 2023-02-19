from django.urls import path
from . import views
urlpatterns = [
    path('',views.ValidStudent.as_view()),
]
