#!/usr/bin/python2
# coding: utf-8

# The comments above allow you to use foreign letters that are found in Spanish
# or any language when running this file from the command line
import sys
import unittest
import os

sys.path.insert(0, "src")

from parser import process

class TestSum(unittest.TestCase):

    # Test example 1
    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    # Test example 2
    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")

    # First test attempt for SymGiza output
    def test_parse_symgiza_output(self):
        data = process()

        print sys.path
        self.assertEqual(data, [('Y', 'and'), ('sus', 'their'), ('children', 'niños')])
        # You're failed test output should look something like this:
        # + [('Y', 'and'), ('sus', 'their'), ('children', 'ni\xc3\xb1os')]
        # - ['1\n',
        # -  '31 11 Y sus ni\xc3\xb1os # 1 2 3\n',
        # -  '25 11 And their little # 1 2 3\n']

if __name__ == '__main__':
    unittest.main()
