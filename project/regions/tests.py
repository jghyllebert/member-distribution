from django.test import TestCase
from .models import Region


class RegionTestCase(TestCase):

    def setUp(self):
        pass

    def test_create_region(self):
        belgium = Region.objects.create(name="Belgium", tva_percentage=21.00)
        netherlands = Region.objects.create(name="Netherlands", tva_percentage=21.00)

        belgium.save()
        netherlands.save()

        self.assertEqual(belgium.tva_percentage, 21.00)