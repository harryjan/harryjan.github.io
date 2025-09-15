#!/usr/bin/env python3
import os
from bs4 import BeautifulSoup

def update_casestudy_html(file_path):
    """
    Updates case study HTML files to a consistent format.
    - Replaces old CSS links with 'common.css' and 'case_studies_articles.css'.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'html.parser')

        made_changes = False

        # --- Stylesheet Link Cleanup ---
        head = soup.find('head')
        if head:
            # Find all old stylesheet links that need replacing
            old_links = head.find_all('link', rel='stylesheet', href=lambda href: href and ('style.css' in href or 'article.css' in href))
            if old_links:
                # Remove all old links
                for link in old_links:
                    link.decompose()
                
                # Create the new, correct links
                common_css_link = soup.new_tag('link', rel='stylesheet', href='../styles/common.css')
                casestudies_css_link = soup.new_tag('link', rel='stylesheet', href='../styles/case_studies_articles.css')
                
                # Find the last <link> tag to insert the new ones after
                # This helps keep the new links at the end of the other links.
                all_links = head.find_all('link', href=True)
                if all_links:
                    last_link_tag = all_links[-1]
                    last_link_tag.insert_after(casestudies_css_link) # Insert new specific CSS
                    last_link_tag.insert_after(common_css_link)
                else: # If no links exist, just append them to head
                    head.append(common_css_link)
                    head.append(casestudies_css_link)
                made_changes = True

        if made_changes:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(str(soup.prettify()))
            print(f"Updated file: {file_path}")
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

def main():
    """Walks through the 'case_studies' directory and updates all HTML files."""
    case_studies_dir = '/Users/harryhunter/Documents/my-portfolio/case_studies'
    # Exclude sub-landing pages which should use case_studies.css, not case_studies_articles.css
    exclude_files = ['thekey.html', 'atkinsrealis.html']
    
    print("Starting to update case study CSS links...")
    for filename in os.listdir(case_studies_dir):
        if filename.endswith('.html'):
            if filename in exclude_files:
                print(f"Skipping excluded file: {filename}")
                continue
            file_to_update = os.path.join(case_studies_dir, filename)
            update_casestudy_html(file_to_update)
    print("...Finished updating case study CSS links.")

if __name__ == "__main__":
    main()
