from articles.api.views import ArticleViewset
from rest_framework.routers import DefaultRouter
# from articles.api.views import ArticleListView, ArticleDetailView,ArticleCreateView, ArticleUpdateView, ArticleDeleteView


router = DefaultRouter()
router.register(r'',ArticleViewset,basename='articles')
urlpatterns = router.urls






# urlpatterns = [
#     path('',ArticleListView.as_view()),
#     path('<pk>/',ArticleDetailView.as_view()),
#     path('create/',ArticleCreateView.as_view()),
#     path('<pk>/update',ArticleUpdateView.as_view()),
#     path('<pk>/delete',ArticleDeleteView.as_view())
# ]