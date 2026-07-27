#!/usr/bin/env python3
import os
import sys
import re

# Import central configuration
sys.path.insert(0, os.path.dirname(__file__))
from config import BASE_DIR, GA_MEASUREMENT_ID

def update_analytics_in_file(file_path, new_id):
    """
    Updates the Google Analytics tracking code in a given HTML file.
    It replaces old IDs and ensures there is only one correct config line.

    Args:
        file_path (str): The path to the HTML file.
        new_id (str): The new GA4 Measurement ID to use (e.g., 'G-XXXXXXXXXX').
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        original_content = content
        
        # Regex finds all gtag('config', '...') lines.
        config_pattern = re.compile(r"gtag\('config', 'G(TM)?-[A-Z0-9]+'\);")
        config_lines = config_pattern.findall(content)

        if config_lines:
            content = config_pattern.sub(f"gtag('config', '{new_id}');", content, 1)
            
            remaining_configs = config_pattern.findall(content)
            if len(remaining_configs) > 0:
                 content = config_pattern.sub("", content)
                 content = content.replace("gtag('js', new Date());", f"gtag('js', new Date());\n\n      gtag('config', '{new_id}');")

        # Also replace the ID in the script src URL
        content = re.sub(r'id=GTM-[A-Z0-9]+', f'id={new_id}', content)

        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content)
            print(f"Updated analytics tag in: {file_path}")

    except Exception as e:
        print(f"Error processing {file_path}: {e}")

def main():
    """Main function to run the script."""
    portfolio_directory = BASE_DIR
    new_measurement_id = GA_MEASUREMENT_ID

    print(f"Updating GA tag across HTML files using ID '{new_measurement_id}'...")
    for root, _, files in os.walk(portfolio_directory):
        for filename in files:
            if filename.endswith('.html'):
                file_path = os.path.join(root, filename)
                update_analytics_in_file(file_path, new_measurement_id)
    print("\nAnalytics tag update complete.")

if __name__ == "__main__":
    main()