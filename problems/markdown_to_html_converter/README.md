# Markdown to HTML Converter

A Python command-line application that converts Markdown (`.md`) files into HTML (`.html`) documents. It supports common Markdown formatting features and automatically generates a complete HTML document.

## Features

- Convert Markdown headings (H1 to H6) into HTML headings.
- Convert paragraphs into HTML paragraph elements.
- Support bold and italic text formatting.
- Convert unordered Markdown lists into HTML lists.
- Support inline code formatting.
- Convert fenced code blocks into HTML code blocks.
- Convert Markdown links into clickable HTML links.
- Escape special HTML characters for safer output.
- Automatically generate an HTML file alongside the original Markdown file.
- Handle invalid file paths, unsupported file extensions, and empty files.
- Handle file permission and encoding errors.

## Technologies Used

- Python 3
- `os` module
- `re` module
- `html` module

All modules used are part of Python's standard library. No external packages are required.

## Project Structure

```text
markdown_to_html_converter/
│
├── main.py
├── sample.md
├── sample.html
└── README.md
```

**Note:** `sample.md` is the sample input file, and `sample.html` is generated automatically after conversion.

## How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/aadityaraj0611-ops/python-learning.git
   ```

2. Navigate to the repository:

   ```bash
   cd python-learning
   ```

3. Run the application:

   ```bash
   python3 problems/markdown_to_html_converter/main.py
   ```

4. Select option `1` to convert a Markdown file.

5. Enter the path of your Markdown file.

   Example:

   ```text
   problems/markdown_to_html_converter/sample.md
   ```

6. The converted HTML file will be generated automatically in the same directory.

## Menu Options

1. Convert Markdown file
2. Exit

## Example

**Markdown Input:**

```markdown
# Python Learning

Python is a **powerful** programming language.

- Variables
- Loops
- Functions

`print("Hello World")`
```

**Generated HTML:**

```html
<h1>Python Learning</h1>
<p>Python is a <strong>powerful</strong> programming language.</p>
<ul>
<li>Variables</li>
<li>Loops</li>
<li>Functions</li>
</ul>
<p><code>print("Hello World")</code></p>
```

## Concepts Practiced

- Functions
- Loops and conditional statements
- String manipulation
- Lists
- Regular expressions
- File handling
- Exception handling
- HTML generation
- Input validation
- Python standard library modules

## Limitations

This project implements a basic Markdown converter rather than the complete Markdown specification. It supports the formatting features listed above, but does not currently support tables, ordered lists, images, or nested lists.

## Author

Aditya Raj