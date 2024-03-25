import shutil

def copy_file(source, destination):
    try:
        shutil.copy(source, destination)
        print(f"File copied from '{source}' to '{destination}'")
    except FileNotFoundError:
        print("File not found!")
    except IsADirectoryError:
        print("Source is a directory. Please provide the path to a file.")
    except shutil.SameFileError:
        print("Source and destination are the same file.")
    except PermissionError:
        print("Permission denied. Check your file permissions.")

# Example usage
source_file = "source.txt"
destination_file = "destination.txt"

copy_file(source_file, destination_file)
