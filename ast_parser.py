import ast

class ASTParser:
    """Parses Python files and extracts class methods using Abstract Syntax Trees."""

    @staticmethod
    def parse_code(code):
        """Parses the given code into an AST."""
        return ast.parse(code)

    @staticmethod
    def get_class_methods_code(ast_node):
        """Extracts methods' code from a given AST node."""
        methods_code = {}
        for node in ast.walk(ast_node):
            if isinstance(node, ast.ClassDef):
                for item in node.body:
                    if isinstance(item, ast.FunctionDef):
                        key = f"{node.name}.{item.name}"
                        methods_code[key] = ast.unparse(item)
        return methods_code


