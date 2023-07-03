-------------------------------------

# Duplicate File Finder

This Python script is designed to search for duplicate files within a selected directory and its subdirectories. It specifically targets files with the extension `.ymap` that start with the prefix "hei_". The script utilizes the `os` module for directory traversal, `defaultdict` for efficient storage of file names and paths, `tkinter` for a directory selection dialog, and `logging` for logging the duplicate file information.

## Features

- Walks through a directory and its subdirectories to find files with a specific extension and prefix.
- Logs the filenames and their paths if they appear more than once in the selected directory.
- Supports custom file extensions for searching duplicate files.
- Provides a simple and user-friendly directory selection dialog using tkinter.

## Usage

1. Run the script.
2. A directory selection dialog will appear.
3. Choose the directory where you want to search for duplicate files.
4. The script will search for files with the specified extension and prefix in the selected directory.
5. Duplicate files will be logged in the file named `duplicates.log`.

## How to Run

To run the script, follow these steps:

1. Clone the repository to your local machine.
2. Make sure you have Python 3 installed.
3. Install the required dependencies by running `pip install -r requirements.txt`.
4. Execute the script by running `python script.py`.
5. Follow the on-screen instructions to select a directory and search for duplicate files.

## License

This project is licensed under the MIT License.

Feel free to use, modify, and distribute this script according to the terms of the license.

## Contributions

Contributions to this project are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## Author

Kyle

## Acknowledgments

Special thanks to the developers and contributors of the `os`, `defaultdict`, `tkinter`, and `logging` modules for providing the necessary tools to create this script.

-------------------------------------
