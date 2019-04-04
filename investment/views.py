import datetime

from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from investment.models import Loan, Investment
from investment.serializers import LoanSerializer, BidSerializer


class LoanList(APIView):

    def get(self, request, format=None):
        if request.data['bank_id']:
            loans = Loan.objects.filter(bank_id=request.data['bank_id'])
        else:
            loans = Loan.objects.filter(status=1)
        serializer = LoanSerializer(loans, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = LoanSerializer(data=request.data)
        serializer.initial_data['status'] = 1
        serializer.initial_data['time_duration_in_auction'] = 1440
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoanDetail(APIView):

    def get_object(self, pk):
        try:
            return Loan.objects.get(pk=pk)
        except Loan.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        loan = self.get_object(pk)
        serializer = LoanSerializer(loan)
        return Response(serializer.data)

    # open auction or bid a loan
    def post(self, request, pk, format=None):
        loan = self.get_object(pk)
        if loan.status == 1:
            bid = {
                'amount': request.data['amount'],
                'interest_rate': request.data['interest_rate'],
                'date_time': datetime.datetime.now(),
                'loan': pk,
                'investor': request.data['investor_id']
            }
            serializer = BidSerializer(data=bid)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    def put(self, request, pk, format=None):
        loan = self.get_object(pk)
        serializer = LoanSerializer(loan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        loan = self.get_object(pk)
        loan.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class InvestmentList(APIView):

    def post(self, request, format=None):
        investments = Investment.objects.filter(bid__investor_id=request.data['investor_id'])
        serializer = LoanSerializer(investments, many=True)
        return Response(serializer.data)
