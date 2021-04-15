import os


def check_import_order():
    os.system("isort --check ./bentoml_test/ --skip __init__.py --gitignore --dont-follow-links --verbose")


def check_code_formatting():
    os.system("black --check ./bentoml_test/ --exclude __init__.py --verbose")


def sort_import_order():
    os.system("isort ./bentoml_test/ ./tests/ --skip __init__.py --gitignore --dont-follow-links --verbose")


def do_code_formatting():
    os.system("black ./bentoml_test/ ./tests/ --exclude __init__.py --verbose")


def linter():
    os.system("pylama ./bentoml_test/ ./tests/")


def run_tests():
    os.system("pytest ./tests/ --verbose --color=yes --code-highlight=yes")
