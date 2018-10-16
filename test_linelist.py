import unittest

from linelist import linelist

class TestLineList(unittest.TestCase):
    def test_makeempty(self):
        li = linelist()
        # don't need anything else, it is causes an error that will fail the test

    def test_addone(self):
        li = linelist()
        li.add('line 1')

#     def test_addtwo(self):
#         li = linelist()
#         li.add('line 1')
#         li.add('line 2')
# 
#     def test_getcount(self):
#         li = linelist()
#         li.add('line 1')
#         li.add('line 2')
#         self.assertEqual(li.get_length(),2)
# 
#     def test_getboth(self):
#         li = linelist()
#         li.add('line 1')
#         li.add('line 2')
#         self.assertEqual(li.get_list(),['line 1','line 2'])
