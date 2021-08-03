from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status

from books.books_api.models import BooksModel
from books.books_api.serializers import BookSerializers


class BookListCreate(APIView):
    def get(self, request):
        books = BooksModel.objects.all()
        serializer = BookSerializers(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        book_serializer = BookSerializers(data=request.data)
        if book_serializer.is_valid():
            book_serializer.save()
            return Response(book_serializer.data, status=status.HTTP_201_CREATED)
        return Response(book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookGetUpdateDelete(APIView):
    def put(self, request, book_id):
        book = get_object_or_404(BooksModel, pk=book_id)
        serializer = BookSerializers(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def get(self, request, book_id):
        try:
            book = BooksModel.objects.get(id=book_id)
            book_serializer = BookSerializers(book)
            return Response(book_serializer.data, status=status.HTTP_200_OK)

        except:
            return Response({"message": "Not found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, book_id):
        try:
            book = BooksModel.objects.get(id=book_id)
            book.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        except:
            return Response({"message": "Not found"}, status=status.HTTP_404_NOT_FOUND)
