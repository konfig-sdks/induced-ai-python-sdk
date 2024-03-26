# coding: utf-8

"""
    Autonomous API

    Building the next evolution of actionable AI.

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

import unittest

import os
from pprint import pprint
from induced_ai_python_sdk import InducedAi

class TestSimple(unittest.TestCase):
    def setUp(self):
        pass

    def test_client(self):
        inducedai = InducedAi(
        
                        api_key_auth = 'YOUR_API_KEY',
        )
        self.assertIsNotNone(inducedai)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()