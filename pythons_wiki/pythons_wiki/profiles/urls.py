from django.urls import path

from pythons_wiki.profiles.views import profile_details

urlpatterns = [
    path('', profile_details, name='profile details'),
]

import pythons_wiki.profiles.signals
