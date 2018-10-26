import unittest

from fileops import fileops
# to learn about learn about using files in python see https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

class TestFileOps(unittest.TestCase):
    def test_save(self):
        # make a class called fileops that has a method call save
        filer = fileops()
        self.assertTrue(filer.save("test1.txt","This is a test file\n"))

#     def test_load(self):
#       # make a class called fileops that has a method call load
#         filer = fileops()
#         self.assertEqual(filer.load("test1.txt"),"This is a test file\n")
# 
#     def test_savetwo(self):
#         filer = fileops()
#         self.assertTrue(filer.save("test2.txt","This is a second test file\n"))
# 
#     def test_loadtwo(self):
#         filer = fileops()
#         self.assertEqual(filer.load("test2.txt"),"This is a second test file\n")
# 
#     def test_getlist(self):
#       # make a method called getFileList that returns a list of all files,
#       # the list should include the tests made above
#       # to find how to get a file list look for os.listdir()
#         filer = fileops()
#         filelist = filer.getFileList()
#         for fname in ['test1.txt','test2.txt']:
#             self.assertIn(fname, filelist)
# 
