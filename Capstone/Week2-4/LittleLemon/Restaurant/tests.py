from django.test import TestCase
from Restaurant.models import MenuItem
# Create your tests here.
class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(id = 3, title="IceCream", price=80, inventory=100)
        self.assertEqual(item, "IceCream : 80")