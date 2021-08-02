from django.urls import path

from article.articles_app.views import ArticlesListView, ArticleCreateView, SourceCreateView, SourceDetailsView, SourcesListView

urlpatterns = (
    path('', ArticlesListView.as_view(), name='index'),
    path('articles/create/', ArticleCreateView.as_view(), name='create article'),
    path('sources/', SourcesListView.as_view(), name='list sources'),
    path('sources/<int:pk>', SourceDetailsView.as_view(), name='details source'),
    path('source/create/', SourceCreateView.as_view(), name='create source'),
)
