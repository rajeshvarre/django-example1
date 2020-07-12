import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first.settings')

import django
# Import settings
django.setup()

import random
from first_app.models import Topic,Webpage,AccessRecord,nam
from faker import Faker

fakegen = Faker()
topics = ['Search','Social','Marketplace','News','Games']

def add_topi():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t



def populate(N=5):
    '''
    Create N Entries of Dates Accessed
    '''

    for entry in range(N):

        # Get Topic for Entry
        top = add_topi()

        # Create Fake Data for entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()


        # Create new Webpage Entry
        webp = Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

        # Create Fake Access Record for that page
        # Could add more of these if you wanted...
        accRec = AccessRecord.objects.get_or_create(name=webp,date=fake_date)[0]

def mady(N=5):
    for entry in range(N):
        fake_names = fakegen.name().split()
        fake_first = fake_names[0]
        fake_last = fake_names[1]
        fake_email = fakegen.email()
        na = nam.objects.get_or_create(first=fake_first, last=fake_last,email=fake_email)[0]
if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    mady(5)
#  populate(10)
    print('Populating Complete')

