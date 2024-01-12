import os, sys
import unittest
import shutil

# Add the parent directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.project import create_structure, Project


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
            ".gitignore"
        ]
    }

    def setUp(self):
        self.project_path = os.path.join(os.getcwd(), "test_project") 

    def tearDown(self):
        # Clean up the test_project directory after each test
        shutil.rmtree(self.project_path)
    
    def test_folder_structure_creation(self):
        prj = Project("test_project", self.project_path)
        prj.initialize_folder_file_structure()
        # create_structure(self.folder_structure, self.project_path)

        # Verify the existence of files and folders
        actual_rel_paths = set()
        for root, dirs, files in os.walk(self.project_path):
            for name in files:
                actual_rel_paths.add(os.path.relpath(os.path.join(root, name), self.project_path))

        expected_rel_paths = {
            os.path.join('test_project', '__init__.py'),
            os.path.join('test_project', 'main.py'),
            os.path.join('test_project', 'module1', '__init__.py'),
            os.path.join('test_project', 'module1', 'file1.py'),
            os.path.join('test_project', 'module2', '__init__.py'),
            os.path.join('test_project', 'module2', 'file2.py'),
            os.path.join('test_project', 'utils', '__init__.py'),
            os.path.join('test_project', 'utils', 'helper_functions.py'),
            os.path.join('tests', '__init__.py'),
            os.path.join('tests', 'test_module1.py'),
            os.path.join('docs'),
            os.path.join('requirements.txt'),
            os.path.join('README.md'),
            os.path.join('.gitignore')
        }
        self.assertEqual(actual_rel_paths, expected_rel_paths)
        gitignore_path = os.path.join(self.project_path, '.gitignore')

        with open(gitignore_path, 'r') as gitignore_file:
            gitignore_contents = gitignore_file.read()

        # Check if gitignore is empty
        self.assertTrue(len(gitignore_contents) == 0)
       
    def test_download_gitignore(self):
        prj = Project("test_project", self.project_path)
        prj.initialize_folder_file_structure()
        prj.download_gitignore()
        
        gitignore_path = os.path.join(self.project_path,'.gitignore')

        with open(gitignore_path, 'r') as gitignore_file:
            gitignore_contents = gitignore_file.read()

        # Check if gitignore is empty
        self.assertTrue(len(gitignore_contents) > 0)
        
         
        
if __name__ == '__main__':
    unittest.main()