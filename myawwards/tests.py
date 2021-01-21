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

# Testing Save Method
    def test_save_method(self):
        self.coco.save_profile()
        coco = Profile.objects.all()
        self.assertTrue(len(coco) > 0)

    def tearDown(self):
        Profile.objects.all().delete()
        

class ProjectTestClass(TestCase):
    def setUp(self):
        self.delani = Project( title  = 'delani', description = 'my tests', photo = '/',  link = 'github.com', design='5', usability ='6', content = '7',vote_submissions= '7')

# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.delani,Project))


