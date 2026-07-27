# harryjan.github.io

Personal website, writing archive, and portfolio for **Harry Jan**. Hosted on [GitHub Pages](https://harryjan.github.io).

---

## 🚀 Overview

This repository contains the static web pages, custom styling, writing collection, and case studies for Harry Jan's personal site. It also includes a suite of Python maintenance scripts in `utility/` to handle common workflows like Substack article imports, header synchronization across HTML pages, and CSS batch updates.

---

## 📁 Repository Structure

```text
.
├── index.html            # Main portfolio landing page
├── books.html            # Book recommendations / reading list page
├── case_studies.html     # Index of case studies
├── consulting.html       # Consulting services page
├── cv.html               # Curriculum Vitae / Resume page
├── writing.html          # Main writing / blog listing page
├── assets/               # Images, media, and downloadable static files
├── styles/               # CSS stylesheets
├── writing/              # Article HTML files
├── case_studies/         # Individual case study pages
├── utility/              # Python maintenance and helper scripts
│   ├── sync_headers.py           # Syncs site header navigation across HTML files
│   ├── import_substack.py        # Imports RSS feed entries from Substack into static pages
│   ├── update_article_css.py     # Updates CSS links and head tags across article templates
│   ├── update_casestudy_css.py   # Updates CSS links across case study pages
│   ├── add_analytics.py          # Inserts Google Analytics snippet into pages
│   ├── update_analytics_tag.py   # Updates tracking tags across HTML files
│   └── fix_links.py              # Audits and cleans up relative links
├── GEMINI.md             # Developer guidelines & architectural context
├── todo.md               # Maintenance roadmap and backlog tracking
└── requirements.txt      # Python dependencies for utility scripts
```

---

## 🛠️ Local Development & Maintenance Setup

### Prerequisites

- A web browser (or local static server tool like Python's `http.server`)
- Python 3.8+ (for utility scripts)

### Setting Up Python Environment for Utility Scripts

1. **Clone the repository:**
   ```bash
   git clone https://github.com/harryjan/harryjan.github.io.git
   cd harryjan.github.io
   ```

2. **Set up a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🛠️ Utility Scripts Guide

The Python scripts in the `utility/` folder help keep HTML templates and styles synchronized.

### Synchronizing Headers Across Pages
To sync navigation updates from `index.html` across all subpages:
```bash
python3 utility/sync_headers.py
```

### Importing Articles from Substack
To import recent articles from Substack RSS:
```bash
python3 utility/import_substack.py <substack_rss_url>
```

### Updating Analytics / Tracking Tags
```bash
python3 utility/add_analytics.py
```

---

## 🚢 Deployment

This site is hosted via GitHub Pages. Any commits pushed to the `main` branch are automatically deployed by GitHub Pages.

---

## 📄 Documentation & Guidelines

For project guidelines, coding conventions, and architectural context, see [GEMINI.md](GEMINI.md).
