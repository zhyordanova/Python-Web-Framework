from rest_framework import serializers

from books.books_api.models import BookModel


class BookSerializers(serializers.ModelSerializer):
    def validate(self, data):
        if data['title']:
            if not data['title'][0].isupper():
                raise serializers.ValidationError('Title must start with capital letter')

        return data

    class Meta:
        model = BookModel
        fields = '__all__'
