import shutil
from pathlib import Path
import sys

# List of possible extensions
FOLDERS = []

def read_and_sort_files(source_path: Path):
    # Function takes path to the source directory and copy/sort files to destination directory

    for path in source_path.iterdir():

        # If it is dir make recursion
        if(path.is_dir()):
            read_and_sort_files(path)
        
        # If it is file call function to copy it to destination directory
        if(path.is_file()):
            copy_files_to_dest(path)


def copy_files_to_dest(source: Path):
    # Function takes path to the source directory and copy files to destination directory by extensions

    destination = ''

    # Check if there was entered destination directory
    try:
        destination = sys.argv[2]
    except:
        destination = 'dist'

    suffix_of_file = source.suffix

    destination = Path(destination + f"/{suffix_of_file}")

    # Check if suffix in the list, if it is not, append it to the list and create dir
    if(suffix_of_file not in FOLDERS):
        FOLDERS.append(suffix_of_file)
        destination.mkdir(parents=True)

    # Copy file
    shutil.copy(source, destination)

    # Print info about copying file
    print(f'Copied from {source.name} to {destination.name} directory')


def main():
    try:
        path_source_dir = Path(sys.argv[1])
        path_dest_dir = Path('dist')

        # Check if there was entered destinatio directory
        try:
            path_dest_dir = Path(sys.argv[2])
        except:
            print("Files would be sorted in 'dist' directory")

        # Check if the path is dir
        if(path_source_dir.is_file()):
            raise ValueError

        # Print name of search dir
        print(f'Copied and sorted from {path_source_dir.name} to {path_dest_dir.name} directory')

        read_and_sort_files(path_source_dir)

    except:
        print('Something went wrong. Please check path!')
    

if __name__ == '__main__':
    main()