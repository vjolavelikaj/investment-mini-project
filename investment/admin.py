from django.contrib import admin

from investment.models import Loan, Bid, Investment

admin.site.register(Loan)
admin.site.register(Bid)
admin.site.register(Investment)
