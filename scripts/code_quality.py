import os


def check_import_order():
    os.system("isort --check ./bentoml-test/ --skip __init__.py --gitignore --dont-follow-links --verbose")


def check_code_formatting():
    os.system("black --check ./bentoml-test/ --exclude __init__.py --verbose")


def sort_import_order():
    os.system("isort ./bentoml-test/ ./tests/ --skip __init__.py --gitignore --dont-follow-links --verbose")


def do_code_formatting():
    os.system("black ./bentoml-test/ ./tests/ --exclude __init__.py --verbose")


def linter():
    os.system("pylama ./bentoml-test/ ./tests/")


def run_tests():
    os.system("pytest ./tests/ --verbose --color=yes --code-highlight=yes")
