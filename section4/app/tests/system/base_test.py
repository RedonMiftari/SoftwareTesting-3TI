from unittest import TestCase
from app.app import app

class BaseTest(TestCase):
    def setUp(self):
        app.testing = True # Tijdens dat de app runned zegt dit tegen Flask dat we in testing mode zijn
        self.app = app.test_client