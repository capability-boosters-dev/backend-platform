import unittest
import xmlrunner
import os
import glob

class TestFolderContentAvailable(unittest.TestCase):
      
    
    def test_alsfile_exists(self):
        template_als_file = glob.glob('*.als')
        self.assertGreaterEqual(template_als_file.__len__(), 1, 'Theres one ALS file there')


if __name__ == '__main__':
    #unittest.main()
    unittest.main(testRunner = xmlrunner.XMLTestRunner(output='test-reports'))