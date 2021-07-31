from django.urls import path

from pythons_wiki.pythons_auth.views import sign_out, SingUpView, SignInView

urlpatterns = [
    # path('sign-up/', sign_up, name='sign up'),
    path('sign-up/', SingUpView.as_view(), name='sign up'),
    # path('sign-in/', sign_in, name='sign in'),
    path('sign-in/', SignInView.as_view(), name='sign in'),
    path('sign-out/', sign_out, name='sign out'),
]
