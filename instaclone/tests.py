from django.test import TestCase
from .models import Profile,Post,Comment,Follow

class FollowTestClass(TestCase):
    def setUp(self):
        self.bett=Follow(username='bett',followed='willy')
                            
    def test_instance(self):
        self.assertTrue(isinstance(self.bett,Follow))

class CommentTestClass(TestCase):
    def setUp(self):
        self.first=Comment(post=1,
                            username='bett',
                            comment='great',
                            date='Sept 14, 2021, 12:41 p.m.',
                            count=0)

    def test_instance(self):
        self.assertTrue(isinstance(self.first,Comment))