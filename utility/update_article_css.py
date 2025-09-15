#!/usr/bin/env python3
import os
from bs4 import BeautifulSoup

def update_article_html(file_path):
    """
    Updates article HTML files to a consistent format.
    - Cleans up the header structure to remove duplicate profile information.
    - Replaces 'style.css' and 'article.css' with 'common.css' and 'writing_articles.css'.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'html.parser')

        made_changes = False

        # --- Header Cleanup ---
        # Find and remove the extra profile picture from article headers
        extra_profile_pic = soup.select_one('header > img.profile-pic')
        if extra_profile_pic:
            extra_profile_pic.decompose()
            made_changes = True

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
                common_css_link = soup.new_tag('link', rel='stylesheet', href='../../styles/common.css')
                articles_css_link = soup.new_tag('link', rel='stylesheet', href='../../styles/writing_articles.css')
                
                # Find the last <link> tag to insert the new ones after
                last_link_tag = head.find_all('link', href=True)[-1]
                last_link_tag.insert_after(articles_css_link)
                last_link_tag.insert_after(common_css_link)
                made_changes = True

        if made_changes:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(str(soup))
            print(f"Updated file: {file_path}")
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

def main():
    """
    Walks through the 'writing' directory and updates all HTML files.
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    portfolio_root = os.path.dirname(script_dir)
    writing_dir = os.path.join(portfolio_root, 'writing')
    
    print("Starting to update article CSS links...")
    for root, _, files in os.walk(writing_dir):
        for file in files:
            if file.endswith('.html'):
                file_to_update = os.path.join(root, file)
                update_article_html(file_to_update)
    print("...Finished updating article CSS links.")

if __name__ == "__main__":
    main()