from django.urls import path

from cats.cats_app.views import show_cats, index, IndexView, ShowCatsView, CatCreateView

urlpatterns = (
    path('', index, name='index'),
    path('cbv/index/', IndexView.as_view(), name='cbv index'),
    path('cats/', show_cats, name='show cats'),
    path('cbv/cats/', ShowCatsView.as_view(), name='cbv show cats'),
    path('create/', CatCreateView.as_view(), name='create cat')
)
