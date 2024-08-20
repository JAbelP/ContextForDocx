# Document Search and Context Finder
This Python program scans a selected directory, reads through all document files, and searches for specific words or phrases within them. If you search for a term like "temper tantrum," all documents containing the term will be returned along with the sentences in which the term appears. Double-clicking on any of these sentences will open the corresponding document.

## Features

### Directory Scanning
Recursively scans the selected directory to locate all document files.

### Text Search
Searches for specific words or phrases in all documents within the directory.

### Contextual Results
Displays the sentences containing the search term, along with the document's name.

### Quick Access
Double-clicking a sentence opens the corresponding document for further review.
Supported Document Formats
.txt
.docx

## Installation
Clone the repository:
```
git clone https://github.com/yourusername/document-searcher.git
cd document-searcher
```
Ensure you have Python 3.x installed on your system. You can download it from python.org.

Install required Python libraries by running the following command:

```
pip install python-docx easygui
```
These libraries are necessary for handling .docx files and providing a simple graphical user interface.

## Configuration

### first run
the program will prompt you to select a directory to scan. This directory will be saved in a config.txt file for future use.
If a config.txt file already exists, the program will automatically use the directory specified in that file.
Search for a term:

Enter the search term or phrase in the input box when prompted.
The program will search all .docx files in the specified directory for the term.

### Open Document:

Double-clicking or selecting a sentence will open the corresponding document for further review.
Dependencies
Python 3.7+: Make sure Python is installed on your system.
python-docx: A library for creating, modifying, and extracting information from .docx files.
easygui: A module for simple GUI operations like message boxes and file dialogs.
To install the dependencies, use:

```
pip install python-docx easygui
```

## Usage
Run the program:
```
python main.py
```

## Future Enhancements
Enhanced PDF Support: Improved text extraction from complex PDF files.
Additional File Formats: Support for .odt, .rtf, and other document formats.
Search Filters: Case sensitivity, whole word matching, etc.
## Contributing
Contributions are welcome! Please fork the repository, create a new branch, and submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
Special thanks to all the contributors and open-source projects that made this tool possible.

