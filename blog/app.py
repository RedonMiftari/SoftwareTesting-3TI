# Eerst dicionary aanmaken met dict()
blogs = dict()     # blog_name : Blog object

def menu():
    #Show user available blogs
    #Let user make choice
    # Do something with that choice
    # Eventually exit

    print_blogs()

def print_blogs():

    for key, blog in blogs.items():
        print(blog)
