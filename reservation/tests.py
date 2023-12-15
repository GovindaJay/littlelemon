from django.test import TestCase

from reservation.models import Menu

class MenuTest (TestCase):

    def test_get_item(self):
        item = Menu.objects.create(title ="IceCream", price = 2.99, inventory =100)
        # itemstr =item.get_item()
        
        self.assertEqual (str(item), "IceCream -- Price $2.99")