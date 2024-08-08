from rest_framework import serializers

from .models import spentAmount

class Spendingserializer(serializers.ModelSerializer):
    class Meta:
        model = spentAmount
        fields = '__all__'
       