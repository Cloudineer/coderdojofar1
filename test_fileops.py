import unittest

from fileops import fileops

class TestFileOps(unittest.TestCase):
    def test_save(self):
        filer = fileops()
        self.assertTrue(filer.save("test1.txt","This is a test file\n"))

#     def test_load(self):
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
#         filer = fileops()
#         filelist = filer.getFileList()
#         for fname in ['test1.txt','test2.txt']:
#             self.assertIn(fname, filelist)
# 
