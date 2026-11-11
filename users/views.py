from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializer, UserSerializer
from .permissions import AdminPermission
from django.shortcuts import get_object_or_404


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


class UserListView(generics.ListAPIView):
    queryset = get_user_model().objects.all().order_by("id")
    serializer_class = UserSerializer
    # Restrict to only admin users
    permission_classes = [AdminPermission]


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [AdminPermission]

    def get_object(self):
        queryset = self.get_queryset()

        obj = get_object_or_404(queryset, **self.kwargs)
        return obj
