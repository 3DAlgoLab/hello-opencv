# Development Guidelines for hello-opencv

## Build, Lint, and Test Commands

### Running Tests
- **Run all tests**: `python -m pytest` (if pytest is configured)
- **Run a single test file**: `python -m pytest path/to/test_file.py`
- **Run a specific test function**: `python -m pytest path/to/test_file.py::test_function_name`
- **Run tests with coverage**: `python -m pytest --cov=src`

### Linting and Formatting
- **Check code style**: `ruff check .` or `flake8 .`
- **Auto-format code**: `ruff format .` or `black .`
- **Type checking**: `mypy .` or `pyright .`

### Build Commands
- **Install dependencies**: `uv sync`
- **Build package**: `uv build`
- **Install in development mode**: `uv pip install -e .`

## Python Rules
- **Python 3.11+** required
- ALWAYS use the virtual environment created by `uv` or run scripts with `uv run`
- Never run Python commands directly without activating the venv or using uv run
- To install python package, always use uv framework. Try `uv add <package-name>` or `uv pip install <package-name>`
- Use modern Python features (match/case, walrus operator, etc.)

## Code Style Guidelines

### Imports
- Group imports in order: standard library, third-party, local
- Use explicit relative imports for local modules
- Import full module names for clarity (e.g., `import cv2` rather than `from cv2 import imread`)
- Sort imports alphabetically within each group
- Avoid wildcard imports (`from module import *`)

### Formatting
- Use 4 spaces for indentation (no tabs)
- Maximum line length of 88 characters
- Use PEP 8 style conventions
- Place imports at the top of the file
- Use blank lines to separate logical sections

### Type Hints
- Add type hints for all function parameters and return values
- Use standard typing annotations (e.g., `List[str]`, `Optional[int]`)
- Prefer `typing` module over string annotations when possible
- Include docstrings with parameter descriptions and return types

### Naming Conventions
- Use snake_case for variables and functions
- Use PascalCase for classes
- Use UPPER_CASE for constants
- Use descriptive names that clearly indicate purpose
- Avoid single-letter variable names except for loop counters

### Error Handling
- Use try/except blocks to handle expected exceptions
- Provide meaningful error messages
- Log errors appropriately using standard logging module
- Don't ignore exceptions silently
- Use specific exception types when possible

### OpenCV Specific Guidelines
- Import cv2 at the top of files
- Check if images loaded successfully before processing (e.g., `if image is not None:`)
- Handle image dimensions properly using `image.shape`
- Use appropriate OpenCV functions for operations (e.g., `cv2.imread`, `cv2.imshow`)

## Cursor/Copilot Rules

### Cursor Rules
- All Python code must follow PEP 8 style guidelines
- Functions should have docstrings explaining their purpose, parameters, and return values
- Variables should be named descriptively to improve readability
- Prefer explicit variable names over abbreviations
- Use consistent indentation and spacing throughout the codebase

### Copilot Instructions
- When generating code, follow the existing project structure and patterns
- Maintain consistency with existing imports and naming conventions
- Ensure all functions are properly typed with type hints
- Add appropriate error handling for file operations
- Use OpenCV's standard practices for image loading and processing