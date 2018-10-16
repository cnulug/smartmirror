# file: openpage_test.py
#
# author: Eric Miers
# version: 10/15/2018
#
# desc: Testclass for openpage.py

import sys, os
import unittest
import src
from src import handler
from src.openpage import openPage

class TestHandler(unittest.TestCase):

    def test_can_open_page_returns_200(self):
        file = "../display_pages/pages/commands_list.html"
        self.assertEqual(openPage(file), 200)

    def test_cannot_open_page_returns_400(self):
        file = "../../display_pages/pages/commands_list.html"
        self.assertEqual(openPage(file), 400)

if __name__ == '__main__':
    unittest.main()
