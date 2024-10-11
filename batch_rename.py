import os

def rename_files_in_directory(directory, find_str, replace_str):
    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        # Check if the file contains the string to find
        if find_str in filename:
            # Create the new filename by replacing the string
            new_filename = filename.replace(find_str, replace_str)
            new_filename = new_filename.lower()
            # Get full paths for the old and new filenames
            old_filepath = os.path.join(directory, filename)
            new_filepath = os.path.join(directory, new_filename)
            
            # Rename the file
            os.rename(old_filepath, new_filepath)
            print(f'Renamed: {filename} -> {new_filename}')
            
# Example usage:
directory = os.getcwd()  # Replace with the directory you want to process
find_str = "_rounded"           # The string you want to find (e.g., space)
replace_str = ""        # The string you want to replace it with (e.g., underscore)

# Run the function
rename_files_in_directory(directory, find_str, replace_str)
