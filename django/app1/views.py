from datetime import datetime, timedelta
from rest_framework import viewsets
from rest_framework.response import Response
from .models import spentAmount
from .serializers import Spendingserializer

class SpendingViewset(viewsets.ModelViewSet):
    queryset = spentAmount.objects.all()
    serializer_class = Spendingserializer

    def get_queryset(self):
        queryset = super().get_queryset()
        period = self.request.query_params.get('period', None)
        today = datetime.now().date()
        
        if period == 'daily':
            start_date = today - timedelta(days=1)
            end_date = today
            queryset = queryset.filter(Date__range=[start_date, end_date])
        elif period == 'weekly':
            start_date = today - timedelta(days=7)
            end_date = today
            queryset = queryset.filter(Date__range=[start_date, end_date])
        elif period == 'monthly':
            start_date = today - timedelta(days=30)
            end_date = today
            queryset = queryset.filter(Date__range=[start_date, end_date])
        elif period == 'yearly':
            start_date = today - timedelta(days=365)
            end_date = today
            queryset = queryset.filter(Date__range=[start_date, end_date])
        
        return queryset
