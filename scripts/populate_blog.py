from blog.models import Blog, Author, Content
from django.contrib.auth.models import User


def populate():

    user = User.objects.get(username='user')
    author = Author.objects.get(user=user)

    content_1 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum"
    content_2 = "Felis eget velit aliquet sagittis id consectetur purus ut faucibus. In arcu cursus euismod quis. Sollicitudin tempor id eu nisl nunc. Platea dictumst vestibulum rhoncus est. Elementum eu facilisis sed odio morbi quis commodo. Sapien nec sagittis aliquam malesuada. Et netus et malesuada fames ac turpis egestas. Tincidunt dui ut ornare lectus sit amet. Elit ullamcorper dignissim cras tincidunt lobortis feugiat. Euismod nisi porta lorem mollis aliquam ut. Magnis dis parturient montes nascetur ridiculus mus. Tellus rutrum tellus pellentesque eu tincidunt tortor aliquam nulla. Mollis aliquam ut porttitor leo. Cursus metus aliquam eleifend mi in. Vel fringilla est ullamcorper eget nulla facilisi. A erat nam at lectus urna."

    number_of_contents = 10
    number_of_blogs = 50
    for blog_id in range(number_of_blogs):
        all_contents = Content.objects.all()

        blog = Blog.objects.create(title=f'Title {blog_id}', blogger=author)

        for content_id in range(number_of_contents):
            content = Content.objects.create(text=content_1 if content_id %
                                             2 == 0 else content_2)
            blog.content_set.add(content)
        blog.save()

        print(f'Blog {blog_id} saved.')


def remove_all():
    Content.objects.all().delete()
    Blog.objects.all().delete()
