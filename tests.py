from django.test import TestCase
from radmin.utils import *
from radmin.console import *

class TestUtils(TestCase):
    def test_radmin_import(self):
        """ testing loading a module by string """
        impo = radmin_import('radmin.views.sample')
        self.assertEqual(impo(), 'Hi there!')
