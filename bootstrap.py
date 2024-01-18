import argparse
from utils import project as project_module

def main():
    # Parse the command-line arguments 
    parser = argparse.ArgumentParser(description='A script with command-line arguments.')
    parser.add_argument("prj_name", help='Name of your project')
    parser.add_argument('-prj_dst', help='Destination of your project')
     
    args = parser.parse_args()


    # Create the project folder
    ## TODO: !if! this gets additional features consider to introduce a projectbuilder class  
    name = args.prj_name
    directory = args.prj_dst 
    if not directory:
        directory = name
        print ("no directory was set, using project name as folder location: ", directory)
    print ("Started bootstrapping at: ", directory)
    project = project_module.Project(name, directory)
    project.initialize_folder_file_structure()
    project.write_main_py()
    project.download_gitignore()
    project.create_venv()
    
    
if __name__ == "__main__":
    main()