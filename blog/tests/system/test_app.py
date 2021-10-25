from unittest import TestCase
from unittest.mock import patch # Patch gaat ons de methodes laten veranderen
from blog import Blog
import app  #kan ook geschreven worden als from app import *,
            # maar door alleen app te importeren
            # hebben we een betere overzicht
            # over welke methode van wekle package is


#Deze test maakt een blog aan en
# patched de print functie van app.py met de mock_print
# Dan roept die deze op via de assert_called_with
class AppTest(TestCase):
    def test_print_blogs(self):
        blog = Blog('Test', 'Test Author')
        app.blogs = {'Test': blog}
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with('- Test by Test Author (0 posts)')