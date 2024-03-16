from open_ai_client import OpenAIClient
import json


class DocumentationGenerator:
    """Generates documentation for Python methods using the OpenAI API."""

    @staticmethod
    def extract_function_calls_from_code(code):
        """Extracts function calls from the given code."""
        client = OpenAIClient.get_client()
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            response_format={"type": "json_object"},
            messages=[
                {"role": "system",
                 "content": """extract function calls from given function and give output as json. Only give functions not arguements.
                        Json format structure should be like this:
                        { 'function_calls': [ fn_name1, fn_name2 ] }
                        """},
                {"role": "user", "content": code}
            ]
        )
        data = response.choices[0].message.content
        data = json.loads(data)
        function_calls = data['function_calls']
        return function_calls

    @staticmethod
    def get_context_code_from_fn_name_to_code_dict(fn_name_to_code_dict):
        context_code = ""
        for fn_name in fn_name_to_code_dict:
            context_code += fn_name_to_code_dict[fn_name] + "\n"
        return context_code

    @staticmethod
    def get_documentation_from_open_ai(code, fn_name_to_code_dict):
        client = OpenAIClient.get_client()
        prompt = f"""
        main code: {code}
        Below is context code
        context code: {DocumentationGenerator.get_context_code_from_fn_name_to_code_dict(fn_name_to_code_dict)}
        """

        response = client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            temperature=0.5,
            messages=[
                {"role": "system",

                 "content": """You are excellent documentation writer. Your job is to assist user with writing documentation for code.
                 Generate documentation for main code. Functions which are used in main code are given as context code below.
                    You will be given main code and helper code. Main code is the code for which you have to generate documentation.
                    You have to write documentation for main code only. You can use helper code to understand the context of main code.
                    Format of documentation should be 
                    - what the function does, should be able to clearly explain the purpose of the function.
                    - what are the inputs
                    - what are the outputs
                    """},
                {"role": "user", "content": prompt}
            ]
        )

        data = response.choices[0].message.content
        return data

    @staticmethod
    def get_fn_name_to_code_dict(all_methods_code_dict, function_calls):
        fn_name_to_code_dict = {}
        for function_call in function_calls:
            if function_call in all_methods_code_dict:
                fn_name_to_code_dict[function_call] = all_methods_code_dict[function_call]['code']
        return fn_name_to_code_dict

    @staticmethod
    def get_documentation_for_function(fn_name, all_methods_code_dict):
        """Generates documentation for a given function name."""
        code = all_methods_code_dict[fn_name]['code']
        function_calls = DocumentationGenerator.extract_function_calls_from_code(code)
        fn_name_to_code_dict = DocumentationGenerator.get_fn_name_to_code_dict(all_methods_code_dict, function_calls)
        documentation = DocumentationGenerator.get_documentation_from_open_ai(code, fn_name_to_code_dict)
        return documentation

        # Additional steps to generate documentation...
