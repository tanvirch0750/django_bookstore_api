
# method 3 - shotcut
from rest_framework import viewsets

from .models import BookStoreModel
from .serializers import BookStoreSerializer


class BookListView(viewsets.ModelViewSet):
    queryset = BookStoreModel.objects.all()
    serializer_class = BookStoreSerializer




# Method 2 - concrete api view

# from rest_framework import generics

# from .models import BookStoreModel
# from .serializers import BookStoreSerializer


# class BookListView(generics.ListCreateAPIView): # get, post
#     queryset = BookStoreModel.objects.all()
#     serializer_class = BookStoreSerializer


# class BookListUpdateDelete(generics.RetrieveUpdateDestroyAPIView): # single get, delete, update
#     queryset = BookStoreModel.objects.all()
#     serializer_class = BookStoreSerializer



# Method one - Api view

# from django.http import Http404
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView

# from .models import BookStoreModel
# from .serializers import BookStoreSerializer


# class BookListView(APIView):
#     """
#     List all snippets, or create a new snippet.
#     """
#     def get(self, request, format=None):
#         model = BookStoreModel.objects.all()
#         serializer = BookStoreSerializer(model, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = BookStoreSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
    
    
    
# class BookListUpdateDelete(APIView):
  
#     def get_object(self, pk):
#         try:
#             return BookStoreModel.objects.get(pk=pk)
#         except BookStoreModel.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = BookStoreSerializer(snippet)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = BookStoreSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
