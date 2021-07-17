from django.shortcuts import render, redirect

from phones_media_files.phones_app.models import Phone
from phones_media_files.phones_app.forms import PhonesForm


def index(request):
    phones = Phone.objects.all()

    for phone in phones:
        phone.selected_image = phone.phoneimage_set.filter(is_selected=True)\
            .first()
        pass

    context = {
        'phones': phones,
        'form': PhonesForm(),
    }

    return render(request, 'index.html', context)


def create_phone(request):
    form = PhonesForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('index')
