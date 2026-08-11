from django.shortcuts import render
from rest_framework.generics import (CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView)
from core.models import Retsept
from core.permissions import IsOwner
from core.serializers import RegisterSerializer, RetseptSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer

class RetseptListCreateAPIView(ListCreateAPIView):
    serializer_class = RetseptSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Retsept.objects.filter(egasi=self.request.user)
        qiyinlik_darajasi = self.request.query_params.get("qiyinlik_darajasi")
        maksimal_vaqt = self.request.query_params.get("maksimal_vaqt")

        if qiyinlik_darajasi:
            queryset = queryset.filter(qiyinlik_darajasi = qiyinlik_darajasi)
        if maksimal_vaqt:
            queryset = queryset.filter(pishirish_vaqti__lte = maksimal_vaqt)

        return queryset

    def perform_create(self, serializer):
        serializer.save(egasi=self.request.user)

class RetseptRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = RetseptSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    queryset = Retsept.objects.all()