#!/usr/bin/env python3
import os
import sys
import re

# Import central configuration
sys.path.insert(0, os.path.dirname(__file__))
from config import BASE_DIR, WRITING_DIR

patterns_to_fix = {
    re.compile(r'href="\.\./(?!(\.\./))([^"]*)"'): r'href="../../\2"',
    re.compile(r'src="\.\./(?!(\.\./))([^"]*)"'): r'src="../../\2"',
}

def fix_article_paths(file_path):
    """
    Reads a file, replaces incorrect relative paths, and writes it back.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content
        
        for pattern, replacement in patterns_to_fix.items():
            content = pattern.sub(replacement, content)

        content = content.replace('src="../../profile.png"', 'src="../../assets/profile.png"')
        content = content.replace('href="../article.css"', 'href="../../article.css"')

        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated: {file_path}")
        else:
            print(f"No changes needed for: {file_path}")

    except Exception as e:
        print(f"Error processing {file_path}: {e}")

def main():
    """
    Walks through the writing/ directory and fixes files in subdirectories.
    """
    print(f"Scanning '{WRITING_DIR}' for article path fixes...")
    for root, dirs, files in os.walk(WRITING_DIR):
        if root != WRITING_DIR:
            for file in files:
                if file.endswith('.html'):
                    file_path = os.path.join(root, file)
                    fix_article_paths(file_path)

if __name__ == "__main__":
    main()
