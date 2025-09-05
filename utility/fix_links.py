#!/usr/bin/env python3
import os
import re

# The root directory of your portfolio
# The script assumes it's running from the same directory as the 'writing' folder.
ROOT_DIR = os.getcwd() 
WRITING_DIR = os.path.join(ROOT_DIR, 'writing')

# Patterns to find and replace.
# We're looking for hrefs and srcs that start with '../' but not '../../'
# This is a simple but effective way to target the incorrect paths.
patterns_to_fix = {
    # For links like href="../index.html" or href="../article.css"
    re.compile(r'href="\.\./(?!(\.\./))([^"]*)"'): r'href="../../\2"',
    # For images like src="../profile.png"
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
        
        # Apply all find-and-replace patterns
        for pattern, replacement in patterns_to_fix.items():
            content = pattern.sub(replacement, content)

        # A specific fix for the profile image which is now in assets
        content = content.replace('src="../../profile.png"', 'src="../../assets/profile.png"')
        # A specific fix for the article.css which is now in the root
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
    print("Starting to scan for article files to fix...")
    # We walk through all directories and files in the 'writing' folder
    for root, dirs, files in os.walk(WRITING_DIR):
        # We only want to process files in subdirectories of 'writing'
        if root != WRITING_DIR:
            for file in files:
                if file.endswith('.html'):
                    full_path = os.path.join(root, file)
                    fix_article_paths(full_path)
    print("...Finished fixing article links.")

if __name__ == "__main__":
    main()
