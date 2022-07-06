import unittest
from unittest.mock import Mock
from postYT import *
import sqlalchemy as db
import pandas as pd

class TestpostYT(unittest.TestCase):
    #test to see if get channel will return string
    def test_get_Channel(self):
        self.assertEqual(type(get_channel()), type(" "))
    
    #test to see if it will return custom string error if channel is not in youtubes data base
    def test_create_info_table(self):
        self.assertEqual(create_info_table({}),type(" "))

    


if __name__ == '__main__':
    unittest.main()