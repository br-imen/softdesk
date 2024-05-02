from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.authtoken.models import Token
from .models import User
from .serializers import  UserSerializer

'''
APIView Method: 

from rest_framework.views import APIView

class UserAPIView(APIView):
    # Get all users
    def get(self, request, format=None):
        # Retrieve all users from the database
        users = User.objects.all()
        # Serialize the user data
        serializer = UserSerializer(users, many=True)
        # Return the serialized data as a response
        return Response(serializer.data)

    # Create a new user
    def post(self, request, format=None):
        # Deserialize the request data using UserSerializer
        serializer = UserSerializer(data=request.data)
        # Check if the data is valid
        if serializer.is_valid():
            # Save the validated data to create a new user
            serializer.save()
            # Return the serialized data of the created user as a response
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # If data is not valid, return error messages
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Update an existing user
    def put(self, request, pk, format=None):
        # Retrieve the user object based on the provided pk (primary key)
        user = self.get_object(pk)
        # Deserialize the request data using UserSerializer and pass the user object for update
        serializer = UserSerializer(user, data=request.data)
        # Check if the data is valid
        if serializer.is_valid():
            # Save the validated data to update the user
            serializer.save()
            # Return the serialized data of the updated user as a response
            return Response(serializer.data)
        # If data is not valid, return error messages
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete an existing user
    def delete(self, request, pk, format=None):
        # Retrieve the user object based on the provided pk (primary key)
        user = self.get_object(pk)
        # Delete the user object
        user.delete()
        # Return a success response
        return Response(status=status.HTTP_204_NO_CONTENT)

        
        in urls.py:
        [...
            path('api/users/', UserAPIView.as_view()),
            path('api/users/<int:pk>/', UserAPIView.as_view()),
        ]

'''



class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

