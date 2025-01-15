from pathlib import Path
import sys

def main():
    try:
        path = Path(sys.argv[1])

        # Check if the path is dir
        if(path.is_file()):
            raise ValueError

        # Print name of search dir
        print(f'Copied from {path.name} to {path.name} directory')

    except:
        print('Something went wrong. Please check path!')
    

if __name__ == '__main__':
    main()