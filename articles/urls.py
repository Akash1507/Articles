from django.urls import path

from articles.views import ArticleListView, ArticleDetailView

urlpatterns = [
    path('',ArticleListView.as_view()),
    path('<pk>',ArticleListView.as_view())
]