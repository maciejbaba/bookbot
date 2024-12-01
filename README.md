# BookBot

BookBot is a simple Python script that generates a report for a given text file, including word count and letter frequency.

---

## Features

- Counts the total number of words in the document.
- Analyzes the frequency of each alphabetic character, ignoring case and special characters.

---

## Usage

1. Place your text file in the `books/` directory.
2. Update the script to point to your desired file (e.g., `frankenstein.txt`).
3. Run the script:
   ```bash
   python bookbot.py
   ```
4. View the report output directly in the terminal.

---

## Example Output

For `books/frankenstein.txt`:

```
--- Begin report of books/frankenstein.txt ---
12345 words found in the document
The 'a' character was found 567 times
The 'b' character was found 234 times
...
--- End report ---
```

---

## Requirements

- Python 3.x
- Text files to analyze

---

## Customization

- Replace `books/frankenstein.txt` with your file path to analyze other books.
- Modify the script to handle additional analytics as needed.

---
