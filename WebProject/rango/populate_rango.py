import os
import django

def populate():
    python_cat = add_cat('Python')

    add_page(cat=python_cat,
        title="Official Python Tutorial",
        url="http://docs.python.org/2/tutorial/",
        views=23)

    add_page(
        cat=python_cat,
        title="How to Think like a Computer Scientist",
        url="http://www.greenteapress.com/thinkpython/",
        views=290)

    add_page(
        cat=python_cat,
        title="Learn Python in 10 Minutes",
        url="http://www.korokithakis.net/tutorials/python/",
        views=45)

    django_cat = add_cat("Django")

    add_page(
        cat=django_cat,
        title="Official Django Tutorial",
        url="https://docs.djangoproject.com/en/1.5/intro/tutorial01/",
        views=9)

    add_page(
        cat=django_cat,
        title="Django Rocks",
        url="http://www.djangorocks.com/",
        views=77)

    add_page(
        cat=django_cat,
        title="How to Tango with Django",
        url="http://www.tangowithdjango.com/",
        views=999)

    frame_cat = add_cat("Other Frameworks")

    add_page(
        cat=frame_cat,
        title="Bottle",
        url="http://bottlepy.org/docs/dev/",
        views=567)

    add_page(
        cat=frame_cat, title="Flask", url="http://flask.pocoo.org", views=5678)

    # Print out what we have added to the user.
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title, url=url, views=views)[0]
    return p


def add_cat(name):
    views = 0
    likes = 0
    if (name == 'Python'):
        views = 128
        likes = 64
    elif (name == 'Django'):
        views = 64
        likes = 32
    elif (name == 'Other Frameworks'):
        views = 32
        likes = 16
    c = Category.objects.get_or_create(name=name, views=views, likes=likes)[0]
    return c


if __name__ == "__main__":
    print('Starting Rangoapp population script...')
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rango.settings')
    django.setup()  # 这一步很关键

    from rangoapp.models import Category, Page
    # Page.objects.all().delete()
    # Category.objects.all().delete()
    populate()