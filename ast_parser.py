import ast

class ASTParser:
    """Parses Python files and extracts class methods using Abstract Syntax Trees."""

    @staticmethod
    def parse_code(code):
        """Parses the given code into an AST."""
        return ast.parse(code)

    @staticmethod
    def get_methods_code(ast_node):
        """Extracts both class methods and non-class methods' code from a given AST node."""
        methods_code = {}

        # Extract class methods
        for node in ast.walk(ast_node):
            if isinstance(node, ast.ClassDef):
                for item in node.body:
                    if isinstance(item, ast.FunctionDef):
                        key = f"{node.name}.{item.name}"
                        methods_code[key] = ast.unparse(item)

        # Extract non-class methods (top-level functions)
        for node in ast.iter_child_nodes(ast_node):
            if isinstance(node, ast.FunctionDef):
                key = node.name
                methods_code[key] = ast.unparse(node)

        return methods_code


