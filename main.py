import os
from collections import defaultdict
import tkinter as tk
from tkinter import filedialog
import logging

def find_duplicate_files(dir_path, extension, use_prefix):
    # Initialize dictionary to hold file names and their paths
    file_dict = defaultdict(list)

    # Walk through directory, including subdirectories
    for dirpath, dirnames, filenames in os.walk(dir_path):
        for filename in filenames:
            # If file has the desired extension and matches the prefix (if enabled), add its path to the dictionary
            if filename.endswith(extension) and (not use_prefix or filename.startswith('hei_')):
                filepath = os.path.join(dirpath, filename)
                file_dict[filename].append(filepath)

    # Log file names that appear more than once and their paths
    for file, paths in file_dict.items():
        if len(paths) > 1:
            for path in paths:
                logging.info(f"File '{file}' found in '{path}'")

def select_directory():
    # Set up logging
    logging.basicConfig(filename='duplicates.log', level=logging.INFO, 
                        format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

    # Hide the main tkinter window
    root = tk.Tk()
    root.withdraw()

    # Open the directory selection dialog
    dir_path = filedialog.askdirectory()

    # If a directory was selected, ask for user preference on prefix usage
    if dir_path:
        use_prefix = input("Include prefix (hei_) in file search? (Y/N): ").lower() == 'y'
        find_duplicate_files(dir_path, '.ymap', use_prefix)

# Run the directory selection
select_directory()
