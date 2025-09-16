#!/usr/bin/env python3
import os

def main():
    """
    Finds all HTML files in the project and inserts the Google Analytics
    tracking snippet before the closing </head> tag.
    """
    # --- Configuration ---
    # IMPORTANT: Replace with your actual Google Analytics Measurement ID.
    ga_measurement_id = "GTM-K2TRN682"
    
    # Hardcoded ID to check for to prevent duplicates from previous failed runs
    previous_ga_id = "GTM-K2TRN682"

    # The Google Analytics snippet to be inserted.
    ga_snippet = f"""    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id={ga_measurement_id}"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){{dataLayer.push(arguments);}}
      gtag('js', new Date());
    
      gtag('config', '{ga_measurement_id}');
    </script>
"""

    # --- Script Logic ---
    project_root = os.path.dirname(os.path.abspath(__file__))
    print("Starting to scan for HTML files...")

    for root, _, files in os.walk(project_root):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r+', encoding='utf-8') as f:
                    content = f.read()
                    
                    # Check if the snippet is already present to avoid duplicates
                    if ga_measurement_id in content or previous_ga_id in content:
                        print(f"GA tag already exists in: {file_path}. Skipping.")
                        continue

                    # Insert the snippet before the </head> tag
                    new_content = content.replace("</head>", f"{ga_snippet}\n</head>", 1)
                    f.seek(0)
                    f.write(new_content)
                    f.truncate()
                    print(f"Adding GA tag to: {file_path}")

    print("Done. Google Analytics tracking script has been added.")

if __name__ == "__main__":
    main()