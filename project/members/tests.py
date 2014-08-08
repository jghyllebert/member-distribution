import random
from django.test import TestCase
import names
from members.management.commands.fill_database import random_region
from personal_shoppers.models import PersonalShopper
from regions.models import Region
from .models import assign_personal_shopper, Member


class CreateMembersTestCase(TestCase):

    def setUp(self):
        self.region = Region.objects.get(name="Belgium")

    def test_random_region_single_region(self):
        """
        Return a random region
        """
        # Only one region, so it should return this one
        self.assertTrue(random_region(), self.region)

    def test_random_region_multiple_regions(self):
        # Create new region
        netherlands = Region.objects.create(name="Netherlands", tva_percentage=21)
        netherlands.save()

        #Return either one
        self.assertTrue(random_region() in Region.objects.all())

    def test_personal_shopper_assignment(self):
        #Create some personal shoppers
        personal_shopper1 = PersonalShopper.objects.create(
            first_name=names.get_first_name(gender="female"),
            last_name=names.get_last_name(),
        )
        personal_shopper2 = PersonalShopper.objects.create(
            first_name=names.get_first_name(gender="female"),
            last_name=names.get_last_name(),
        )

        personal_shopper1.save()
        personal_shopper2.save()

        personal_shopper1.regions.add(self.region)
        personal_shopper2.regions.add(self.region)

        #Create some users without recent orders and assign them to personal shopper 1
        for _ in xrange(5):
            member = Member.objects.create(
                first_name=names.get_first_name(gender='male'),
                last_name=names.get_last_name(),
                phone_number=random.randint(1, 9999999999),
                region=random_region(),
                personal_shopper=personal_shopper1,
            )

            member.save()

        #Check if a new member would be assigned to personal shopper 2
        self.assertEqual(assign_personal_shopper(self.region), personal_shopper2)
