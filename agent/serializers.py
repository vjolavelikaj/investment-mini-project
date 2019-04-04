from rest_framework import serializers

from agent.models import Bank, Investor


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = ('id', 'name', 'location', 'contact')


class InvestorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investor
        fields = ('id', 'name', 'type', 'location', 'contact')
