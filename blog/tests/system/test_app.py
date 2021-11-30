import builtins
from unittest import TestCase
from unittest.mock import patch # Patch gaat ons de methodes laten veranderen
from blog import Blog
import app  # kan ook geschreven worden als from app import *,
            # maar door alleen app te importeren
            # hebben we een betere overzicht
            # over welke methode van wekle package is


# Deze test maakt een blog aan en
# patched de print functie van app.py met de mock_print
# Dan roept die deze op via de assert_called_with
from post import Post


class AppTest(TestCase):
    def test_menu_calls_create_blog(self):
        with patch('builtins.input') as mocked_input:
            with patch('app.ask_create_blog') as mocked_ask_create_blog:
                mocked_input.side_effect = ('c', 'Test Create Blog', 'Test Author','q')

                app.menu()

                mocked_ask_create_blog.assert_called()

    def test_menu_calls_create_post(self):
        with patch('builtins.input') as mocked_input:
            with patch('app.ask_create_post') as mocked_ask_create_post:
                mocked_input.side_effect = ('p', 'Test Blog Name', 'Post Title', 'Llorem Ipsum', 'q')

                app.menu()

                mocked_ask_create_post.assert_called()

    def test_menu_prompt(self):
        with patch('builtins.input') as mocked_input:
            app.menu()
            mocked_input.assert_called_with(app.MENU_PROMPT)


    def test_menu_calls_print_blogs(self):
        with patch('app.print_blogs') as mocked_print_blogs:
            with patch('builtins.input', return_value='q'):
                app.menu()
                mocked_print_blogs.assert_called()

    def test_print_blogs(self):
           blog = Blog('Test', 'Test Author')
           app.blogs = {'Test': blog}
           with patch('builtins.print') as mocked_print:
               app.print_blogs()
               mocked_print.assert_called_with('- Test by Test Author (0 posts)')

    def test_ask_create_blog(self):
        with patch('builtins.input') as mocked_input:

            #Side_effect = gaat meerdere returns herkennen, zoveel params dat je wilt
            mocked_input.side_effect = ('Test', 'Test Author')
            app.ask_create_blog()

            self.assertIsNotNone(app.blogs.get('Test'))


    def test_ask_read_blog(self):
        blog = Blog('Test', 'Test Author')
        app.blogs = {'Test': blog}
        with patch('builtins.input', return_value='Test'):
            app.ask_read_blog()
            with patch('app.print_posts') as mocked_print_posts:
                app.ask_read_blog()

                mocked_print_posts.assert_called_with(blog)

    def test_print_posts(self):
        blog = Blog('Test', 'Test Author')
        blog.create_post('Test post', 'Test Content')
        app.blogs = {'Test': blog}

        with patch('app.print_post') as mocked_print_post:
            app.print_posts(blog)

            mocked_print_post.assert_called_with(blog.posts[0])

    def test_print_pist(self):
        post = Post('Post Title', 'Post Content')
        expected_print = '''
--- Post Title ---
        
Post Content
        
'''
        with patch('builtins.print') as mocked_print:
            app.print_post(post)

            mocked_print.assert_called_with(expected_print)


    def test_ask_create_post(self):
        blog = Blog('Test', 'Test Author')
        app.blogs = {'Test': blog}

        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test', 'Test Title', 'Test Content')

            app.ask_create_post()

            self.assertEqual(blog.posts[0].title, 'Test Title')
            self.assertEqual(blog.posts[0].content, 'Test Content')

