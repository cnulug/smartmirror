# file: handler_test.py
#
# author: Eric Miers
# version: 10/15/2018
#
# desc: Testclass for handler.py

import sys, os
import unittest
import src
from src import handler
from src.handler import commandHandler

class TestHandler(unittest.TestCase):

    def test_unhandled_command_returns_200(self):
        self.assertEqual(commandHandler("This is a test string"), 200)
        #print("TEST 1: ran")

    def test_command_list_returns_201_1(self):
        self.assertEqual(commandHandler("What commands can I ask?"), 201)

    def test_command_list_returns_201_2(self):
        self.assertEqual(commandHandler("Show me commands list"), 201)

if __name__ == '__main__':
    unittest.main()
