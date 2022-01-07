"""
BaseTest

Parent klasse voor elke non-unit testen.
Dit zal ervoor zorgen dat bij elke test zal de databank terug
blank worden en alles dat  tijdens het testen ingevuld
werd zal weggewist worden.

"""

from unittest import TestCase
from starter_code.app import app
from starter_code.db import db

class BaseTest(TestCase):
    def setUp(self):
        # Zeker maken dat databank bestaat
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
        with app.app_context():
            db.init_app(app)  # Databank Initialiseren met app
            db.create_all()  # Zal databank aanmaken met alle nodige data uit item.py
        # Test Client aanmaken
        self.app = app.test_client()
        self.app_context = app.app_context
        pass

    def tearDown(self):
        # Databank is leeg
        with app.app_context():
            db.session.remove()  # Databank stoppen
            db.drop_all() # Databank leeg maken
        pass