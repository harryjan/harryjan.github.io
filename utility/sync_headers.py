#!/usr/bin/env python3
import os
from bs4 import BeautifulSoup

def create_header_html(soup, relative_path_prefix):
    """
    Generates the standard header HTML content with corrected relative paths.
    """
    header = soup.new_tag('header')
    
    h1 = soup.new_tag('h1')
    a_main = soup.new_tag('a', href=f"{relative_path_prefix}index.html")
    a_main.string = "Harry Hunter"
    h1.append(a_main)
    header.append(h1)
    
    nav = soup.new_tag('nav')
    ul = soup.new_tag('ul')

    # Define menu items
    menu_items = {
        "Home": "index.html",
        "Consulting": "consulting.html",
        "CV": "cv.html",
        "Case Studies": "case_studies.html",
        "Writing": "writing.html",
        "Books": "books.html"
    }

    for text, href in menu_items.items():
        li = soup.new_tag('li')
        a = soup.new_tag('a', href=f"{relative_path_prefix}{href}")
        a.string = text
        li.append(a)
        ul.append(li)

    nav.append(ul)
    header.append(nav)
    
    return header

def sync_header_in_file(file_path, root_dir):
    """
    Finds an old header or a placeholder and replaces it with a new,
    standardized static header with correctly adjusted relative links.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'html.parser')

        # Find either the placeholder or an existing header tag
        placeholder = soup.find('div', id='header-placeholder')
        old_header = soup.find('header')
        
        element_to_replace = placeholder or old_header

        # If neither is found, there's nothing to do for this file.
        if not element_to_replace:
            return

        # Calculate the relative path from the file's directory to the root
        file_dir = os.path.dirname(file_path)
        relative_path_to_root = os.path.relpath(root_dir, file_dir)
        
        if relative_path_to_root == '.':
            relative_path_prefix = ''
        else:
            # os.path.join will correctly handle path separators
            relative_path_prefix = os.path.join(relative_path_to_root, '').replace('\\', '/')

        # Generate the new header with correct paths
        new_header = create_header_html(soup, relative_path_prefix)

        # Replace the placeholder with the new header
        element_to_replace.replace_with(new_header)

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(str(soup.prettify()))
        
        print(f"Synced header in: {os.path.relpath(file_path, root_dir)}")

    except Exception as e:
        print(f"Error processing {file_path}: {e}")

def main():
    """Walks through the project directory and syncs headers in all HTML files."""
    portfolio_dir = '/Users/harryhunter/Documents/1_dev_projects/my-portfolio'
    exclude_dirs = {os.path.join(portfolio_dir, 'utility')}

    print("Starting to sync headers across all HTML files...")
    for root, dirs, files in os.walk(portfolio_dir):
        dirs[:] = [d for d in dirs if os.path.join(root, d) not in exclude_dirs]
        for filename in files:
            if filename.endswith('.html'):
                file_path = os.path.join(root, filename)
                sync_header_in_file(file_path, portfolio_dir)
    print("...Finished syncing headers.")

if __name__ == "__main__":
    main()