#!/usr/bin/env python3
import os
import sys

# Import central configuration
sys.path.insert(0, os.path.dirname(__file__))
from config import BASE_DIR, GA_MEASUREMENT_ID

def update_gtag_id_in_file(file_path, old_id, new_id):
    """
    Replaces the old Google Tag ID with the new one in a given file.

    Args:
        file_path (str): The path to the HTML file.
        old_id (str): The placeholder or old GTag ID to be replaced.
        new_id (str): The new GTag ID.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        if old_id not in content:
            return

        new_content = content.replace(old_id, new_id)

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(new_content)
        
        print(f"Successfully updated GTag ID in {file_path} to '{new_id}'.")

    except Exception as e:
        print(f"An error occurred while processing {file_path}: {e}")

def update_all_html_files(directory, old_id, new_id):
    """
    Walks through a directory and updates the GTag ID in all HTML files.

    Args:
        directory (str): The root directory to search for HTML files.
        old_id (str): The placeholder or old GTag ID to be replaced.
        new_id (str): The new GTag ID.
    """
    if not os.path.isdir(directory):
        print(f"Error: Directory '{directory}' not found.")
        return

    print(f"Scanning for HTML files in '{directory}'...")
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith('.html'):
                file_path = os.path.join(root, filename)
                update_gtag_id_in_file(file_path, old_id, new_id)
    print("...Scan complete.")


if __name__ == "__main__":
    portfolio_directory = BASE_DIR
    old_gtag_id = 'G-YOUR_MEASUREMENT_ID'
    new_gtag_id = GA_MEASUREMENT_ID
    
    update_all_html_files(portfolio_directory, old_gtag_id, new_gtag_id)
