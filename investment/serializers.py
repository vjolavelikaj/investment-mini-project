from rest_framework import serializers

from investment.models import Loan, Bid, Investment


class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = (
            'id', 'transaction', 'amount', 'min_interest_rate', 'status', 'created_by', 'time_duration_in_auction')


class BidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bid
        fields = ('id', 'amount', 'interest_rate', 'date_time', 'loan', 'investor')


class InvestmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investment
        fields = ('id', 'amount', 'interest', 'date_time', 'bid')
