# In-Memory File System
## Datastructures used:
In the InMemoryFileSystem implementation, the primary data structure used is a nested dictionary to represent the file system hierarchy.
#### Nested Dictionary:
- Purpose:
Represents the hierarchical structure of directories and files.
Facilitates efficient navigation and storage of the file system.
- Structure:
Keys are full paths of directories or files.
Values are either subdirectories (nested dictionaries) or file content (represented as an empty string in this basic implementation).

## InMemoryFileSystem Overview:
The InMemoryFileSystem is a basic implementation of a file system in Python that operates entirely in memory. It provides a command-line interface for users to interact with the file system, allowing them to perform operations such as creating directories, files, navigating through the hierarchy, and manipulating file content. Here's a brief overview:

#### File System Hierarchy Representation:
The file system is represented as a hierarchical structure using a nested dictionary.
Directories and files are modeled as keys, and their contents are values (either nested dictionaries for directories or empty strings for file content).
#### Supported Operations:
* mkdir(directory_name):
Creates a new directory with the specified name in the current directory.
* cd(path):
Navigates to the specified directory or moves to the parent directory (..).
* touch(file_name):
Creates an empty file with the specified name in the current directory.
* echo('text', 'file.txt'):
Writes the provided text to the specified file.
* rm(target):
Removes the specified file or empty directory.
* cp(source, destination):
Copies the content of one file to another.
* cat(file_name):
Displays the content of the specified file.
#### User Interaction:
The system operates in a loop where the user can input commands.
The run method interprets user input, extracts the operation and arguments, and dynamically invokes the corresponding method.
#### Path Handling:
The system uses the os.path.join and os.path.dirname functions for robust path handling, ensuring platform independence.
#### Error Handling:
Provides error messages for invalid commands or operations, such as creating existing directories/files, navigating to non-existent directories, etc.
#### Data Structures:
The primary data structure is a nested dictionary, representing the hierarchical structure of directories and files.
Strings are used to represent the content of files.
#### Design Decisions:
The system uses a dictionary for its simplicity and efficiency in representing a hierarchical structure.
An empty string represents file content for simplicity in this basic implementation.
#### Extensibility:
The system is designed to be extensible, allowing for the addition of new commands or enhancements to existing functionalities.
#### Platform Independence:
The use of os.path.join and os.path.dirname ensures that the system is platform-independent regarding path handling.
#### Conclusion:
The InMemoryFileSystem provides a basic but functional in-memory file system, serving as a foundation that can be extended and customized for more advanced use cases or integrated into larger applications.
