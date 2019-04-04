from apscheduler.schedulers.background import BackgroundScheduler
from django.db.models import Avg

from investment.models import Bid


def auction_manager():
    return


def invest_in_auction(loan):
    """

    :param loan:
    :return:
    """
    bids = loan.bids.all().order_by('interest_rate', 'date_time')
    remaining_amount = loan.amount
    invest_in_bid = Bid.objects
    for bid in bids:
        if bid.can_create_investment(remaining_amount):
            invest_in_bid.append(bid)
            remaining_amount = bid.decrease_remaining_amount(remaining_amount)
        else:
            break
    if remaining_amount == 0:
        map(bid.confirm_investment(invest_in_bid.aggregate(Avg('interest_rate'))), invest_in_bid)

    else:
        loan.mark_loan_as_not_active()


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(auction_manager(), 'interval', minutes=1)
    scheduler.start()
