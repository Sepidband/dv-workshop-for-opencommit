from models import Step, Codelab

from markdown_parser import parse_markdown

from markdown_parser import parse_markdown
from html_renderer import render

# Example Usage
file_path = 'example.md'  # Replace with your markdown file path
codelab = parse_markdown(file_path)
html_output = render(codelab)

# Writing to example.html
with open('example.html', 'w') as file:
    file.write(html_output)

# Example Usage
file_path = 'example.md'  # Replace with your markdown file path
codelab = parse_markdown(file_path)
print(codelab.title)  # For now, just print the title to test

# print('Hello Project')