
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "user_assignment.settings")
import django
django.setup()
import random
from create_user.models import MyUser
from faker import Faker

fake_gen = Faker()

def populate_users(count=5):
  for i in range(count):
    user = MyUser(firstname=fake_gen.first_name(),lastname=fake_gen.last_name(),email=fake_gen.email()) 
    user.save()


if __name__ == "__main__":
  print("populating scripts....")
  populate_users(10)
  print("population done.")

