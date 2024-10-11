import os

def list_png_files():
    # Get the current working directory
    current_directory = os.getcwd()
    
    # List to store PNG filenames
    png_files = []
    
    # Scan through all files in the directory
    for filename in os.listdir(current_directory):
        # Check if the file has a .png extension
        if filename.lower().endswith('.png'):
            png_files.append(filename)

    # Print the list of PNG files
    if png_files:
        print("PNG Files:")
        for png_file in png_files:
            print(png_file)
    else:
        print("No PNG files found in the current directory.")

# Run the function
list_png_files()
