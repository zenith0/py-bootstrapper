import os, sys
import unittest
import shutil

# Add the parent directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.project import create_structure


class TestFolderStructure(unittest.TestCase):
    folder_structure = {
        "project": [
            "__init__.py",
            {"module1": ["__init__.py", "file1.py"]},
            {"module2": ["__init__.py", "file2.py"]},
            {"utils": ["__init__.py", "helper_functions.py"]},
            "main.py",
            {"tests": ["__init__.py", "test_module1.py"]},
            "docs",
            "requirements.txt",
            "README.md",
        ]
    }

    def setUp(self):
        self.project_path = os.path.join(os.getcwd(), "test_project")
        os.makedirs(self.project_path, exist_ok=True)

    def tearDown(self):
        # Clean up the test_project directory after each test
        shutil.rmtree(self.project_path)
    
    def test_folder_structure_creation(self):
        create_structure(self.folder_structure, self.project_path)

        # Verify the existence of files and folders
        actual_rel_paths = set()
        for root, dirs, files in os.walk(self.project_path):
            for name in files:
                actual_rel_paths.add(os.path.relpath(os.path.join(root, name), self.project_path))

        expected_rel_paths = {
            'project\\__init__.py',
            'project\\module1\\__init__.py',
            'project\\module1\\file1.py',
            'project\\module2\\__init__.py',
            'project\\module2\\file2.py',
            'project\\utils\\__init__.py',
            'project\\utils\\helper_functions.py',
            'project\\main.py',
            'project\\tests\\__init__.py',
            'project\\tests\\test_module1.py',
            'project\\docs',
            'project\\requirements.txt',
            'project\\README.md'
        }

        self.assertEqual(actual_rel_paths, expected_rel_paths)

if __name__ == '__main__':
    unittest.main()