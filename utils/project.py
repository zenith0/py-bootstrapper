import os
import urllib.request
            
# think about "pathbuilder", currently we have the problem that we need some kind of "base path" which
# is extended by the kv pairs.
def create_structure(entry, base_path="."):
    if isinstance(entry, dict):
        for key, value in entry.items():
            folder_path = os.path.join(base_path, key)

            if isinstance(value, list):
                if not os.path.exists(folder_path):
                    print("Creating folder: ", folder_path)
                    os.makedirs(folder_path)

                for item in value:
                    create_structure(item, folder_path)

            elif isinstance(value, str):
                with open(os.path.join(base_path, value), "w") as file:
                    print("Creating file: ", file.name, " at ", base_path)
                    file.write("")
            else:
                create_structure(value, folder_path)

    elif isinstance(entry, str):
        with open(os.path.join(base_path, entry), "w") as file:
            print("Creating file: ", file.name, " at ", base_path)
            file.write("")
    else:
        raise ValueError("Invalid entry type in folder structure.")



# Folder is opt. If not given it takes the name and creates a folder at a relative path
class Project:
    def __init__(self, name, folder=None):
        self.name = name
        if folder is None:
            folder = name
            # Expand ~ to the user's home directory
        expanded_path = os.path.expanduser(folder)
        # Get the absolute path
        full_path = os.path.abspath(expanded_path)
        self.folder = full_path

        
    def initialize_folder_file_structure(self):
        folder_structure = {
            self.folder: [
                {self.name : [
                            "__init__.py", 
                            "main.py",
                            {"module1": ["__init__.py", "file1.py"]},
                            {"module2": ["__init__.py", "file2.py"]},
                            {"utils": ["__init__.py", "helper_functions.py"]}
                            ]
                },
                {"tests": ["__init__.py", "test_module1.py"]},
                "docs",
                "requirements.txt",
                "README.md",
                ".gitignore"
            ]
        }
        print("Configured folder_structure:")
        print(folder_structure)
        print("Creating project files at ", self.folder)
        create_structure(folder_structure, self.folder)
    
    def download_gitignore(self):
        print("Bootstrapping .gitignore...")
        gitignore_url = 'https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore'
        gitignore_path = os.path.join(self.folder, '.gitignore')
        print("Fetching ", gitignore_url, "into", gitignore_path)
        with urllib.request.urlopen(gitignore_url) as response, open(gitignore_path, 'wb') as out_file:
            data = response.read()
            out_file.write(data) 
        



        
        
        