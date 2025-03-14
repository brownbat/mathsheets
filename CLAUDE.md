# MathSheets Developer Guide

## Commands
- **Run server**: `python app.py`
- **Install dependencies**: `pip install -r requirements.txt`
- **Create virtual env**: `python -m venv venv && source venv/bin/activate`

## Code Style
- **Formatting**: Follow PEP 8 standards for Python code
- **Imports**: Group standard library imports first, then third-party, then local
- **Naming**: 
  - snake_case for functions, variables, and modules
  - PascalCase for classes
  - ALL_CAPS for constants
- **Function length**: Keep functions under 30 lines for readability
- **Error handling**: Use try/except blocks with specific exception types
- **Documentation**: Docstrings for functions and modules ("""triple quotes""")

## Problem Generation
- **Duplicates**: Prevent identical problems on the same page
- **Specific Constraints**: Each operation type has custom constraints 
- **Difficulty Levels**: Categorized by educational concepts (carrying, regrouping, etc.)
- **Validation**: Ensure generated problems match their intended category

## Layout Guidelines
- **Problem Format**: Problems are presented vertically with proper alignment
- **Operation Styles**: Division uses table-based layout for clarity
- **Page Structure**: Each page contains 20 problems (4×5 grid)
- **Print Settings**: Headers repeat on each page with page numbers
- **Worksheet Header**: Includes title, operation type, name and date fields

## Architecture
- **Flask**: Web app with clean, print-friendly user interface
- **Template System**: Jinja2 templates with dynamic problem generation
- **Problem Categories**: Specialized subcategories for each operation type