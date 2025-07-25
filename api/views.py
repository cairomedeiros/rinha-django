from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from .serializers import PaymentsSerializer

class PaymentViewSet(viewsets.ViewSet):

    serializer_class = PaymentsSerializer
    
    @action(detail=True, methods=['post'], url_path="payments")
    def payments(self, request):
        valid_data = self.serializer_class(request.data).is_valid()
        if valid_data:
            #se o dado é valido a gente salva no redis .
            return None
    
    @action(detail=True, methods=['get'], url_path="payments-summary")
    def payments_summary(self, request):

        # buscar no redis, aqui teremos 2 campos opicionais to e from, serve pra buscar valores entre 2 datas
        # timestamp no formato ISO em UTC
        return None