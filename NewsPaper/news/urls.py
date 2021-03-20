from django.urls import path
from .views import NewsList, PostDetailView


urlpatterns = [
    path('', NewsList.as_view()),
    path('<int:pk>', PostDetailView.as_view()),
]
