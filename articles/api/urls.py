from django.urls import path

from articles.api.views import ArticleListView

urlpatterns = [
    path('',ArticleListView.as_view()),
    path('<pk>',ArticleListView.as_view())
]