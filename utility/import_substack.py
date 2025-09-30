#!/usr/bin/env python3
import os
import sys
import re
import feedparser
from bs4 import BeautifulSoup
from datetime import datetime

# --- Configuration ---
SUBSTACK_URL = "https://harryhunter.substack.com"
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
TEMPLATE_PATH = os.path.join(ROOT_DIR, 'writing', '_substack_template.html')
OUTPUT_DIR = os.path.join(ROOT_DIR, 'writing', 'substack')
WRITING_PAGE_PATH = os.path.join(ROOT_DIR, 'writing.html')
# --- End Configuration ---

def slugify(text):
    """
    Convert a string into a URL-friendly slug.
    """
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s-]', '', text)  # Remove special characters
    text = re.sub(r'[\s]+', '-', text)       # Replace spaces with hyphens
    text = text.strip('-')
    return text

def clean_html(html_content):
    """
    Cleans the HTML content from Substack's RSS feed to match the site's style.
    """
    soup = BeautifulSoup(html_content, 'html.parser')

    # Remove Substack-specific elements like the subscription buttons
    for element in soup.find_all(class_=re.compile("subscribe-widget")):
        element.decompose()

    # Remove empty paragraphs
    for p in soup.find_all('p'):
        if not p.get_text(strip=True) and not p.find_all('img'):
            p.decompose()

    # Wrap linked images from Substack in a <figure> tag for consistent styling
    for a_tag in soup.find_all('a'):
        if a_tag.find('img') and not a_tag.find_parent('figure'):
            a_tag.wrap(soup.new_tag('figure'))

    # Whitelist of allowed tags and their attributes
    allowed_tags = {
        'p': [], 'h3': [], 'h4': [], 'ul': [], 'ol': [], 'li': [],
        'blockquote': [], 'em': [], 'strong': [], 'hr': [],
        'figure': [],
        'a': ['href', 'target', 'rel'],
        'img': ['src', 'alt', 'height', 'width']
    }

    # Clean all tags
    for tag in soup.find_all(True):
        if tag.name not in allowed_tags:
            # Unwrap the tag if it's not allowed, keeping its content
            tag.unwrap()
        else:
            # Remove all attributes except the whitelisted ones
            allowed_attrs = allowed_tags[tag.name]
            for attr in list(tag.attrs):
                if attr not in allowed_attrs:
                    del tag[attr]

    # Ensure external links open in a new tab
    for a_tag in soup.find_all('a'):
        a_tag['target'] = '_blank'
        a_tag['rel'] = 'noopener noreferrer'

    # Prettify the HTML to make it readable
    return soup.prettify()

def add_to_writing_page(article_title, article_path, publish_date):
    """
    Adds a link to the new article to the main writing.html page.
    """
    print("Adding link to writing.html...")
    try:
        with open(WRITING_PAGE_PATH, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'html.parser')

        # Find the "Newsletter" section and its article list
        newsletter_header = soup.find('h3', string=re.compile(r'\s*Newsletter\s*'))
        if not newsletter_header:
            print("Could not find '<h3>Newsletter</h3>' section in writing.html. Skipping update.")
            return

        article_list = newsletter_header.find_next_sibling('ul', class_='article-list')
        if not article_list:
            # If the list doesn't exist, create it after the newsletter paragraph
            p_tag = newsletter_header.find_next_sibling('p')
            article_list = soup.new_tag('ul', **{'class': 'article-list'})
            p_tag.insert_after(article_list)

        # Create the new list item
        new_li = soup.new_tag('li', **{'class': 'article-item'})
        new_li.string = f"[{publish_date.strftime('%Y-%m-%d')}] "
        new_a = soup.new_tag('a', href=os.path.relpath(article_path, ROOT_DIR).replace('\\', '/'))
        new_a.string = article_title
        new_li.append(new_a)

        article_list.insert(0, new_li) # Prepend to the top of the list

        with open(WRITING_PAGE_PATH, 'w', encoding='utf-8') as f:
            f.write(str(soup.prettify()))

    except Exception as e:
        print(f"Error updating writing.html: {e}")

def main(post_url):
    """
    Main function to fetch, process, and create the article file.
    """
    print("Fetching RSS feed...")
    feed_url = f"{SUBSTACK_URL}/feed"
    feed = feedparser.parse(feed_url)

    if feed.bozo:
        print(f"Error parsing feed: {feed.bozo_exception}")
        return

    target_entry = None
    for entry in feed.entries:
        if entry.link == post_url:
            target_entry = entry
            break

    if not target_entry:
        print(f"Could not find post with URL: {post_url}")
        return

    print(f"Found post: '{target_entry.title}'")

    # --- Extract Data ---
    title = target_entry.title
    link = target_entry.link
    
    # Format date as "Month Day, Year"
    pub_date_parsed = datetime(*target_entry.published_parsed[:6])
    pub_date_formatted = pub_date_parsed.strftime('%B %d, %Y')
    
    # Get the main content
    raw_body = ""
    if 'content' in target_entry and len(target_entry.content) > 0:
        raw_body = target_entry.content[0].value
    else:
        print("Could not find content in the RSS entry.")
        return

    # --- Clean and Prepare ---
    print("Cleaning HTML content...")
    cleaned_body = clean_html(raw_body)

    # --- Generate File ---
    print("Generating new HTML file...")
    try:
        with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
            template_content = f.read()
    except FileNotFoundError:
        print(f"Error: Template file not found at {TEMPLATE_PATH}")
        return

    # Replace placeholders
    final_content = template_content.replace('{{ARTICLE_TITLE}}', title)
    final_content = final_content.replace('{{SUBSTACK_URL}}', link)
    final_content = final_content.replace('{{PUBLISH_DATE}}', pub_date_formatted)
    final_content = final_content.replace('{{ARTICLE_BODY}}', cleaned_body)

    # Create filename
    date_prefix = pub_date_parsed.strftime('%Y-%m-%d')
    slug = slugify(title)
    filename = f"{date_prefix}_{slug}.html"
    output_path = os.path.join(OUTPUT_DIR, filename)

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(final_content)

    print("\nSuccess!")
    print(f"New article created at: {output_path}")
    print("\nNext steps:")
    add_to_writing_page(title, output_path, pub_date_parsed)
    print(f"1. Review the new article: {output_path}")
    print(f"2. Review the updated writing page: {WRITING_PAGE_PATH}")
    print("3. Commit and push the changes if everything looks correct.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python utility/import_substack.py <substack_post_url>")
        sys.exit(1)

    # Before running, you may need to install dependencies:
    # pip install feedparser beautifulsoup4
    
    post_url_arg = sys.argv[1]
    main(post_url_arg)