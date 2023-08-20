from django.test import TestCase
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        MenuItem.objects.create(title="pasta", price=60, inventory=100)
        MenuItem.objects.create(title="bread", price=50, inventory=100)

    def test_getall(self):
        queryset = MenuItem.objects.all()
        serializer = MenuItemSerializer(queryset,many=True)
        self.assertEqual(serializer.data, [{'id': 2, 'title': 'pasta', 'price': '60.00', 'inventory': 100},
                                           {'id': 3, 'title': 'bread', 'price': '50.00', 'inventory': 100}])
        #self.assertEqual(serializer.data, {'id': 3, 'title': 'bread', 'price': '50.00', 'inventory': 100})
        #self.assertEqual(serializer.data, {'id': 2, 'title': 'pasta', 'price': '60.00', 'inventory': 100})

