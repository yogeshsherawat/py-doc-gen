from file_parser import FileParser
from documentation_generator import DocumentationGenerator
from config import DIRECTORY_PATH
from helper import Helper

def main():
    file_parser = FileParser(DIRECTORY_PATH)
    file_parser.build_index()
    fn_name_to_data_dict = file_parser.all_methods_code_dict
    fn_name_to_documentation_dict = {}
    for key in fn_name_to_data_dict:
        documentation = DocumentationGenerator.get_documentation_for_function(key, fn_name_to_data_dict)
        fn_name_to_documentation_dict[key] = documentation
    Helper.dump_json_data_to_json_file(fn_name_to_documentation_dict, "documentation.json")

    # Further code to save or display the documentation...

if __name__ == "__main__":
    main()
