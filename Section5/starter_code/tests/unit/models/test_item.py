from unittest import TestCase

from starter_code.models.item import ItemModel

class ItemTest(TestCase):
    def test_create_item(self):
        item = ItemModel('test', 19.99)

        self.assertEqual(item.name, 'test', "Error - Foute naam") #derde argument mogelijk voor error bericht als test faalt
        self.assertEqual(item.price, 19.99, "Error - Foute prijs")

    def test_item_json(self):
        item = ItemModel('test', 19.99)

        expected = {
            'name' : 'test',
            'price' : 19.99
        }

        self.assertEqual(item.json(), expected, "Error - Foute output")