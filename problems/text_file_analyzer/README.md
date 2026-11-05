# Text File Analyzer

A Python-based project that reads a text file, analyzes its contents, and generates a detailed analysis report.

## Features

- **Character Count:** Counts the total number of characters.
- **Word Count:** Calculates the total number of words.
- **Line Count:** Counts the number of lines.
- **Sentence Count:** Estimates the number of sentences.
- **Unique Words:** Counts the number of distinct words.
- **Word Analysis:** Identifies the longest and shortest words.
- **Word Frequency:** Finds the most frequently occurring word and displays the frequency of each word.
- **Word Search:** Checks whether a particular word exists in the file and displays its occurrence count.
- **Report Generation:** Automatically generates an `analysis_report.txt` file containing the results.
- **Error Handling:** Handles missing files, permission errors, and encoding errors.

## Technologies Used

- Python 3
- String module
- File Handling
- Dictionaries
- Lists
- Functions
- Exception Handling

## Project Structure

```text
text_file_analyzer/
│
├── main.py
├── sample.txt
└── analysis_report.txt
```

## How to Run

1. Open the project folder in VS Code.
2. Open the terminal.
3. Run the following command:

```bash
python3 main.py
```

4. Enter the name of the text file when prompted.

Example:

```text
Enter the text file name: sample.txt
```

5. Enter a word to search for when prompted.

Example:

```text
Enter a word to search: python
```

6. Open `analysis_report.txt` to view the generated analysis.

## Sample Input

**sample.txt**

```text
Python is a powerful programming language.
Python is easy to learn.
I am learning Python programming.
Programming helps solve problems.
```

## Output

The program generates an `analysis_report.txt` file containing:

- File name
- Total characters
- Total words
- Total lines
- Total sentences
- Unique words
- Longest and shortest words
- Most frequent word and its frequency
- Word frequency list
- Word search result

## Learning Outcomes

Through this project, I practiced:

- Reading and processing text files.
- Working with strings and punctuation.
- Using dictionaries to count word frequencies.
- Applying functions to organize code.
- Handling file-related exceptions.
- Generating structured reports automatically.

---

**Project:** Text File Analyzer  
**Language:** Python  
**Author:** Aditya Raj