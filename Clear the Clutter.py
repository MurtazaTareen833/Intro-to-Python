import os

def clear_clutter(folder_path):
    png_files = [file for file in os.listdir(folder_path) if file.endswith('.png')]
    png_files.sort()  # Sort the files alphabetically

    for i, file_name in enumerate(png_files):
        old_path = os.path.join(folder_path, file_name)
        new_name = f"{i + 1}.png"
        new_path = os.path.join(folder_path, new_name)

        # Rename the file
        os.rename(old_path, new_path)
        print(f"Renamed: {file_name} -> {new_name}")

# Example usage
folder_path = "path/to/folder"  # Replace with the actual folder path
clear_clutter(folder_path)
