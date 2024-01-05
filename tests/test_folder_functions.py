import unittest, platform, os
from utils import folder_functions

WIN_VALID_PATH = "C:\\win32"
LINUX_VALID_PATH = "/var/log"

WIN_INVALID_PATH = LINUX_VALID_PATH
LINUX_INVALID_PATH = WIN_VALID_PATH

CONST_WIN = "Windows"
CONST_LINUX = "Linux"
CONST_MAC = ""

path = ""   

class TestFolderFunctions(unittest.TestCase):
    def setUp(self):
        plat = platform.system()
        if plat == CONST_WIN:
            path = WIN_VALID_PATH
        elif plat == CONST_LINUX:
            path = LINUX_VALID_PATH
        print ("Running test on " + plat + "... Using path: " + path)

        
    def test_abspath(self):
        self.assertTrue (folder_functions.abspath(path))
        
    def test_abspath_from_rel(self):
        self.assertEqual(os.path.abspath(os.curdir + "/win32"), folder_functions.abspath("win32"))