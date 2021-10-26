# Eerst dicionary aanmaken met dict()
blogs = dict()     # blog_name : Blog object
MENU_PROMPT = 'Enter "c to create a blog, "l" to list blogs, "r" to read one, "p" to create a post, or "q" to quit'

# '''   ''' betekent multiline quotes in python
POST_TEMPLATE = '''
--- {} ---
        
{}
        
'''

from blog import Blog

def menu():
    #Show user available blogs
    #Let user make choice
    # Do something with that choice
    # Eventually exit

    print_blogs()
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == 'c':
            ask_create_blog()
        elif selection == 'l':
            print_blogs()
        elif selection == 'r':
            ask_read_blog()
        elif selection == 'p':
            ask_create_post()
        selection = input(MENU_PROMPT)

def print_blogs():

    for key, blog in blogs.items():
        print('- {}'.format(blog))

def ask_create_blog():

    #Eerste side_effect (zie test_app)
    title = input('Enter blog title: ')

    #Tweede side_effect (zie test_app)
    author = input('Enter your name: ')

    blogs[title] = Blog(title, author)

def ask_read_blog():
    title = input('Enter blog title: ')

    print_posts(blogs[title])

def print_posts(blog):
    for post in blog.posts:
        print_post(post)

def print_post(post):
    print(POST_TEMPLATE.format(post.title, post.content))


def ask_create_post():
    pass