from unittest import TestCase
from post import Post

class PostTest(TestCase):

    def test_create_post(self):
        p = Post('Test', 'Test Content')

        self.assertEqual('Test', p.title)
        self.assertEqual('Test Content', p.content)

    def test_json(self):
        p = Post('Test', 'Test Content')

        #Hier gaan we een variabele expect aanmaken die een JSON-sequentie voorstelt
        expected = {'title': 'Test', 'content': 'Test Content'}

        #assertDictEqual gaat testen of onze p.json dictionary dezelfde waarde
        #heeft als de JSON-sequentie expected
        self.assertDictEqual(expected, p.json())