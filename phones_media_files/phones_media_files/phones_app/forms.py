from django import forms

from phones_media_files.phones_app.models import Phone, PhoneImage


class PhonesForm(forms.ModelForm):
    image = forms.ImageField()

    def save(self, commit=True):
        phone = super().save(commit=True)

        phone_image = PhoneImage(
            image=self.cleaned_data['image'],
            phone=phone,
            is_selected=True,
        )

        if commit:
            phone_image.save()

    class Meta:
        model = Phone
        fields = '__all__'
