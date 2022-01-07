from starter_code.models.item import ItemModel
from starter_code.tests.base_test import BaseTest


class ItemTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            item = ItemModel('test', 19.99)  #Item aanmaken

            self.assertIsNone(ItemModel.find_by_name('test'))  # # Kijken of de item niet gekend is in de DB

            item.save_to_db() # Item in DB opslaan

            self.assertIsNotNone(ItemModel.find_by_name('test')) #Kijken of de item in de DB te vinden is

            item.delete_from_db() # Item Verwijderen van de DB

            self.assertIsNone(ItemModel.find_by_name('test')) # Kijken of de item niet gekend is in de DB