# Python Code Documentation Generator

## Introduction
This project provides a set of tools for parsing Python files within a specified directory, extracting class methods using Abstract Syntax Trees (AST), and generating documentation for these methods by leveraging the OpenAI API. It is designed to facilitate the automatic generation of detailed documentation for Python projects, improving the efficiency of the development process.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Dependencies](#dependencies)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [Contributors](#contributors)
- [License](#license)

## Installation
To set up this project, follow these steps:

1. Clone the repository to your local machine.
2. Ensure you have Python installed.
3. Install the required dependencies by running `pip install -r requirements.txt`.

## Usage
To use this tool, you'll need to perform the following steps:

1. Configure the `config.py` file with your OpenAI API key and project directory path.
2. Execute the `main.py` script: `python main.py`.
3. The script will parse all Python files in the specified directory (excluding any folders listed in `IGNORE_FOLDERS`), extract methods, and generate documentation using the OpenAI API.

## Features
- **AST-Based Parsing:** Utilizes Python's Abstract Syntax Trees to accurately parse and extract class methods from Python files.
- **OpenAI API Integration:** Generates documentation for extracted methods using the powerful GPT models from OpenAI.
- **Customizable Exclusions:** Allows specifying folders to ignore during the parsing process, such as virtual environments.

## Dependencies
- Python 3.9 or higher
- `ast` — Built-in Python module for working with Abstract Syntax Trees.
- `os` — Built-in Python module for interacting with the operating system.
- `openai` — OpenAI Python client library for accessing OpenAI's API services.

## Configuration
- `OPENAI_API_KEY`: Your OpenAI API key for authentication.
- `IGNORE_FOLDERS`: List of folder names to exclude from the parsing process.
- `DIRECTORY_PATH`: The path to the directory containing the Python files you want to parse and document.



## Troubleshooting
If you encounter issues, check the following:
- Ensure your OpenAI API key is correctly set in `config.py`.
- Verify the `DIRECTORY_PATH` in `config.py` is correct and points to your project directory.
- Confirm all dependencies are installed and up-to-date.

## Contributors
To contribute to this project, please fork the repository and submit a pull request with your proposed changes.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
