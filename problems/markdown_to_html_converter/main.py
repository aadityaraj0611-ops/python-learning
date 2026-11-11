import os
import re
import html

def convert_inline(text):
    # Escape HTML characters first.
    text = html.escape(text)

    # Inline code

    text = re.sub(
        r"`([^`]+)`",
        r"<code>\1</code>",
        text
    )

    # Bold text

    text = re.sub(
        r"\*\*(.+?)\*\*",
        r"<strong>\1</strong>",
        text
    )

    # Italic text
    
    text = re.sub(
        r"\*(.+?)\*",
        r"<em>\1</em>",
        text
    )

    # Markdown links

    text = re.sub(
        r"\[([^\]]+)\]\((https?://[^\s)]+)\)",
        r'<a href="\2">\1</a>',
        text
    )

    return text

def convert_markdown(markdown_text):
    lines = markdown_text.splitlines()
    html_lines = []

    paragraph = []
    list_items = []
    in_code_block = False
    code_lines = []

    def close_paragraph():
        if paragraph:
            content = " ".join(paragraph)
            html_lines.append(
                "<p>" + convert_inline(content) + "<p>"
            )
            paragraph.clear()
    def close_list():
        if list_items:
            html_lines.append("<ul>")

            for item in list_items:
                html_lines.append(
                    "<li>" + convert_inline(item) + "</li>"
                )
            html_lines.append("</ul>")
            list_items.clear()

    for line in lines:
        stripped = line.strip()

        # Cide block handling

        if stripped.startswith(" ' ' "):
            close_paragraph()
            close_list()

            if not in_code_block:
                in_code_block = True
                code_lines = []
            else:
                code_content = "\n".join(code_lines)
                html_lines.append(
                    "<pre><code>"
                    + html.escape(code_content)
                    + "</code></pre>"
                )
                in_code_block = False
            continue
        if in_code_block:
            code_lines.append(line)
            continue
        
        # Empty line
        if stripped == "":
            close_paragraph()
            close_list()
            continue
        
        # Headings
        heading_match = re.match(r"^(#{1,6})\s+(.+)$", stripped)

        if heading_match:
            close_paragraph()
            close_list()

            level = len(heading_match.group(1))
            content = convert_inline(heading_match.group(2))

            html_lines.append(
                f"<h{level}>{content}</h>{level}"
            )
            continue

        # Unordered list
        if stripped.startswith("- ") or stripped.startswith("* "):
            close_paragraph()

            list_items.append(stripped[2:].strip())
            continue

        # Normal Paragraph

        close_list()
        paragraph.append(stripped)

    # Close remaining content
    close_paragraph()
    close_list()

    # Handle an unfinished code block

    if in_code_block:
        code_content = "\n".join(code_lines)
        html_lines.append(
            "<pre><code>"
            + html.escape(code_content)
            + "</code></pre>"
        )
    return "\n".join(html_lines)

def convert_file():
    print("\n--- Markdown to HTMl Converter ---")

    input_file = input("Enter Markdown file path: ").strip()

    if not input_file:
        print("File path cannot be empty.")
        return
    if not os.path.isfile(input_file):
        print("Error: Please provide a .md file.")
        return

    try:
        with open(input_file, "r", encoding="utf-8") as file:
            markdown_text = file.read()
        if not markdown_text.strip():
            print("Error: Markdown file is empty.")
            return

        converted_content = convert_markdown(markdown_text)

        html_docuement = (
            "<!DOCTYPE html>\n"
            "<html>\n"
            "<head>\n"
            '    <meta charset="UTF-8>\n'
            '    <title>Converted Markdown</title>\n'
            "</head>\n"
            "<body>\n"
            + converted_content
            + "\n</body>\n"
            "</html>"
        )
        output_file = os.path.splitext(input_file)[0] + ".html"

        with open(output_file, "w", encoding="utf-8") as file:
            file.write(html_docuement)

        print("\nConversion successfull!")
        print("HTML file saved at:", output_file)
    except PermissionError:
        print("Error: Permission denied while accessing the file.")
    except UnicodeDecodeError:
        print("Error: Could not read the file encoding.")
def main():
    while True:
        print("\n==================================")
        print(".      MARKDOWN TO HTML CONVERTER")
        print("==================================")
        print("1. Convert Markdown file")
        print("2. Exit")

        choice = input("\nEnter your choice (1-2): ")

        if choice == "1":
            convert_file()
        elif choice == "2":
            print("Thank you for using Markdown to HTML Converter!")
            break
        else:
            print("Invalid choice. Please select 1 or 2.")
main()