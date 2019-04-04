from datetime import datetime

from django.db import models

from agent.models import Bank, Investor

STATUS = (
    (1, 'Open'),
    (2, 'Closed')
)


class Loan(models.Model):
    transaction = models.CharField(max_length=50)
    amount = models.FloatField()
    min_interest_rate = models.FloatField()
    status = models.IntegerField(choices=STATUS, null=True)
    created_by = models.ForeignKey(Bank, on_delete=models.PROTECT, related_name='loans', null=False)
    amount_to_bid = models.FloatField(null=True)
    time_duration_in_auction = models.IntegerField()

    class Meta:
        ordering = ('transaction',)

    def __str__(self):
        return self.transaction

    def mark_loan_as_not_active(self):
        self.status = 2
        self.save()


class Bid(models.Model):
    amount = models.FloatField()
    interest_rate = models.FloatField()
    date_time = models.DateTimeField()
    loan = models.ForeignKey(Loan, on_delete=models.PROTECT, related_name='bids', null=False)
    investor = models.ForeignKey(Investor, on_delete=models.PROTECT, related_name='bids', null=False)

    class Meta:
        ordering = ('date_time',)

    def __str__(self):
        return 'Loan : {}, Time of Bid: {}, Amount: {}, Interest: {} '.format(self.loan, self.date_time, self.amount,
                                                                              self.interest_rate)

    def can_create_investment(self, remaining_amount):
        return self.amount <= remaining_amount

    def confirm_investment(self):
        Investment.objects.create(bid=self, date_time=datetime.now())

    def decrease_remaining_amount(self, remaining_amount):
        return remaining_amount - self.amount if remaining_amount - self.amount >= 0 else 0


class Investment(models.Model):
    date_time = models.DateTimeField()
    bid = models.ForeignKey(Bid, on_delete=models.PROTECT, related_name='investments', null=False)
    interest_rate = models.FloatField()

    class Meta:
        ordering = ('date_time',)

    def __str__(self):
        return '{}, Time of Investment: {}'.format(self.bid, self.date_time)
