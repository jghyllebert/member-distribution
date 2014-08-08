from dateutil.relativedelta import relativedelta
from datetime import date
from django.core.management.base import BaseCommand, CommandError
from members.models import Member, Order
from personal_shoppers.models import PersonalShopper
from regions.models import Region

import names
import random


def random_region():
    last_region_id = Region.objects.order_by('-id')[0].id  # Highest id in the database
    random_id = random.randint(1, last_region_id)
    # Get the random id, or the next object if the random id doesn't exist
    return Region.objects.filter(id__gte=random_id)[0]


def random_date():
    current_year_minus_two = date.today().year - 2
    start_date = date.today().replace(year=current_year_minus_two).toordinal()
    end_date = date.today().toordinal()

    return date.fromordinal(random.randint(start_date, end_date))


def create_personal_shoppers(amount):
        for _ in xrange(amount):
            personal_shopper = PersonalShopper.objects.create(
                first_name=names.get_first_name(gender='female'),
                last_name=names.get_last_name(),
            )

            personal_shopper.is_active = bool(random.getrandbits(1))
            personal_shopper.save()
            personal_shopper.regions.add(random_region())


def create_members(amount):
    for _ in xrange(amount):
            member = Member.objects.create(
                first_name=names.get_first_name(gender='male'),
                last_name=names.get_last_name(),
                phone_number=random.randint(1, 9999999999),
                region=random_region(),
            )

            member.save()

    return Member.objects.all()


def create_orders(amount, members):
    for _ in xrange(amount):
        order = Order.objects.create(member=random.choice(members), order_date=random_date())
        order.save()


class Command(BaseCommand):

    def handle(self, *args, **options):
        """
        Empty tables first
        1. Create 10 personal shoppers
        2. Create 50 members
        3. Create 30 orders in the past two years and assign them to random members
        """

        help = 'Generates basic data for app'

        #Start fresh
        PersonalShopper.objects.all().delete()
        Member.objects.all().delete()
        Order.objects.all().delete()

        create_personal_shoppers(10)
        members = create_members(50)
        create_orders(30, members)

        #Get last order for each member
        for member in members:
            try:
                last_order = member.order_set.order_by('-order_date')[0]
                three_months_ago = date.today() + relativedelta(months=-3)
                if last_order.order_date > three_months_ago:
                    member.ordered_recently = True
                    member.save()
            except IndexError:  # No orders yet
                pass