from django.contrib import admin

from phones_media_files.phones_app.models import Phone, PhoneImage


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    pass


@admin.register(PhoneImage)
class PhoneImagesAdmin(admin.ModelAdmin):
    pass
