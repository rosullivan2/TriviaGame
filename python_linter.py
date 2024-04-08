import ast
import os

class PythonLinter(ast.NodeVisitor):
    def __init__(self):
        self.errors = []

    def visit_ClassDef(self, node):
        # Rule 1: Check class names for CapWords convention
        if not node.name[0].isupper():
            self.errors.append(f"Class name '{node.name}' should start with a capital letter. Line: {node.lineno}")

        self.generic_visit(node)

    def visit_FunctionDef(self, node):
        # Rule 1: Check function names for snake_case convention
        if "_" not in node.name:
            self.errors.append(f"Function name '{node.name}' should be in snake_case. Line: {node.lineno}")

        self.generic_visit(node)

    def visit_Import(self, node):
        # Rule 3: Check for unused imports
        for alias in node.names:
            module_name = alias.name.split('.')[0]
            if not any(alias.name in line for line in self.code_lines[node.lineno - 1:]):
                self.errors.append(f"Unused import: '{alias.name}'. Line: {node.lineno}")

        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        # Rule 3: Check for unused imports
        for alias in node.names:
            if not any(alias.name in line for line in self.code_lines[node.lineno - 1:]):
                self.errors.append(f"Unused import: '{alias.name}'. Line: {node.lineno}")

        self.generic_visit(node)

def lint_python_code(code):
    tree = ast.parse(code)
    linter = PythonLinter()
    linter.code_lines = code.split('\n')
    linter.visit(tree)
    return linter.errors

if __name__ == "__main__":
    with open("trivia.py", "r") as python_file:
        python_code = python_file.read()

    errors = lint_python_code(python_code)

    if errors:
        print("Linting failed:")
        for error in errors:
            print(error)
    else:
        print("Linting passed.")
