import os
import shutil

class InMemoryFileSystem:
    def __init__(self):
        self.current_directory = '/'
        self.file_system = {}

    def mkdir(self, directory_name):
        new_directory_path = os.path.join(self.current_directory, directory_name)
        if new_directory_path in self.file_system:
            print(f"Error: Directory '{directory_name}' already exists.")
        else:
            self.file_system[new_directory_path] = {}
            print(f"Directory '{directory_name}' created.")

    def cd(self, path):
        if path == '/':
            self.current_directory = '/'
        elif path == '..':
            # Move to the parent directory
            self.current_directory = os.path.dirname(self.current_directory)
        else:
            # Navigate to the specified path
            new_path = os.path.join(self.current_directory, path)
            if new_path in self.file_system and isinstance(self.file_system[new_path], dict):
                self.current_directory = new_path
            else:
                print(f"Error: Directory '{path}' not found.")


    def touch(self, file_name):
        new_file_path = os.path.join(self.current_directory, file_name)
        if new_file_path in self.file_system:
            print(f"Error: File '{file_name}' already exists.")
        else:
            self.file_system[new_file_path] = ""
            print(f"File '{file_name}' created.")

    # Fix the indentation of the echo method
    def echo(self, *args):
        if len(args) < 2:
            print("Error: Invalid syntax for echo. Usage: echo 'text' file.txt")
            return

        text = ' '.join(args[:-1])
        file_name = args[-1]
        file_path = os.path.join(self.current_directory, file_name)

        if file_path in self.file_system and isinstance(self.file_system[file_path], str):
            self.file_system[file_path] = text
            print(f"Text written to '{file_name}'.")
        else:
            print(f"Error: File '{file_name}' not found.")


    def cat(self, file_name):
        file_path = os.path.join(self.current_directory, file_name)
        if file_path in self.file_system and isinstance(self.file_system[file_path], str):
            print(self.file_system[file_path])
        else:
            print(f"Error: File '{file_name}' not found.")
    def run(self):
        while True:
            command = input(f"\n{self.current_directory}$ ").split()
            if not command:
                continue

            operation = command[0]
            args = command[1:]

            if operation == 'exit':
                print("Exiting the file system.")
                break
            elif hasattr(self, operation):
                getattr(self, operation)(*args)
            else:
                print(f"Error: Invalid operation '{operation}'. Available operations: mkdir, cd, ls, touch, echo, cat, cp, mv, rm, exit")


if __name__ == "__main__":
    file_system = InMemoryFileSystem()
    file_system.run()