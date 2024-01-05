import argparse
from utils import folder_functions

def main():
    # Parse the command-line arguments 
    parser = argparse.ArgumentParser(description='A script with command-line arguments.')
    parser.add_argument('prj_name', type=str, help='Name of your project')
    parser.add_argument('--prj_dir', type=str, help='Your project folder', required=False)
    try: 
        args = parser.parse_args()
    except: 
        print ("no valid directory given, exiting...")
        return

    # Create the project folder
    ## TODO: move to utils?
    name = args.prj_name
    directory = args.prj_dir 
    if not directory:
        print ("no directory was set, using project name as folder location: ", directory)
        directory = name
    directory = folder_functions.abspath(directory)
    print ("Started bootstrapping at: ", folder_functions.abspath(directory))
    if folder_functions.create_project_dir(directory):
        print ("Created project folder: ", directory)
    else: print ("Could not create folder: ", directory, ".. Maybe it already exists?")
    
    
if __name__ == "__main__":
    main()