from django.test import TestCase

# Create your tests here.
from .models import *
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTestClass(TestCase):
    def setUp(self):
        self.coco = Profile( profile_picture  = '/', bio = 'my tests', contact='mahorotesting@gmail.com')

# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.coco,Profile))

  