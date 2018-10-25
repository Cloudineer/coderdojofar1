# test a class which can create, return and edit a list of strings
# in our case the strings will be descriptions of lines to draw on screen
# hence the name linelist. It could be used to any kind of list.

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

#     def test_list_to_string(self):
#         # we need a method to convert a line list into a string (probably to save to a file) 
#         # lookup the command str.join(). NB the joining string is before the .join
#         li = linelist()
#         li.add('line 1')
#         li.add('line 2')
#         self.assertEqual(li.list_to_string(),"line 1\nline 2\n")

#     def test_string_to_list(self):
#         # we need a method to convert a string (probably from a file) into a line list
#         # lookup the command str.split(). You should also know \n means a newline
#         test_string = "line 1\nline 2\n"
#         li = linelist()
#         li.string_to_list(string)
#         self.assertEqual(li.get_list(),['line 1','line 2'])
