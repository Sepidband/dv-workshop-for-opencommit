from models import Step, Codelab

from markdown_parser import parse_markdown

# Example Usage
file_path = 'example.md'  # Replace with your markdown file path
codelab = parse_markdown(file_path)
print(codelab.title)  # For now, just print the title to test

# print('Hello Project')