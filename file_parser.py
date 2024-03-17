import os
from ast_parser import ASTParser
from config import IGNORE_FOLDERS

class FileParser:
    """Parses Python files within a directory, excluding specified folders."""

    def __init__(self, directory_path):
        self.directory_path = directory_path
        self.all_methods_code_dict = {}

    def parse_python_file(self, file_path):
        """Parses a single Python file and updates the methods code dictionary."""
        for folder in IGNORE_FOLDERS:
            if folder in file_path:
                return

        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        parsed_ast = ASTParser.parse_code(content)
        methods_code_dict = ASTParser.get_methods_code(parsed_ast)

        fn_to_data_dict = {key: {'filepath': file_path, 'code': methods_code_dict[key]} for key in methods_code_dict}
        self.all_methods_code_dict.update(fn_to_data_dict)

    def build_index(self):
        """Builds an index of methods from Python files within the directory."""
        for root, dirs, files in os.walk(self.directory_path):
            for file in files:
                if file.endswith('.py'):
                    file_path = os.path.join(root, file)
                    self.parse_python_file(file_path)
