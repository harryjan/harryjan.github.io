# Project Guidelines & Context: harryjan.github.io

## Overview
Personal website and portfolio hosted on GitHub Pages. The repository contains static HTML pages, custom CSS styling, writing/articles, case studies, and Python utility scripts used for site maintenance and content imports.

---

## Directory & File Layout

- **`index.html`**: Portfolio homepage / main landing page.
- **`books.html`**, **`case_studies.html`**, **`consulting.html`**, **`cv.html`**, **`writing.html`**: Core site pages.
- **`styles/`**: CSS stylesheet assets.
- **`assets/`**: Site images, media, and downloadable static assets.
- **`writing/`**: Article HTML files and blog post content.
- **`case_studies/`**: Detailed case study HTML pages.
- **`utility/`**: Maintenance scripts written in Python:
  - `add_analytics.py`: Inserts analytics scripts into HTML pages.
  - `fix_links.py`: Audits/fixes relative links across site pages.
  - `import_substack.py`: Import script for Substack RSS / articles into static pages.
  - `sync_headers.py`: Synchronizes common header navigation components across HTML pages.
  - `update_analytics_tag.py`: Updates existing Google Analytics / tracking tags across HTML files.
  - `update_article_css.py` & `update_casestudy_css.py`: Batch updates CSS dependencies across article and case study templates.
- **`todo.md`**: Maintenance roadmap and backlog tracking.

---

## Development & Conventions

1. **Static HTML/CSS**: Keep pages semantic, accessible, and responsive without heavy external frameworks.
2. **Relative Paths**: Ensure references to assets, styles, and other HTML pages use clean relative paths for standard GitHub Pages hosting.
3. **Utility Scripts**:
   - Always prefer `os.path.dirname(__file__)` and relative path resolution over hard-coded absolute paths.
   - External dependencies (e.g. `beautifulsoup4`, `feedparser`) should be declared in `requirements.txt`.
4. **Maintenance Workflow**:
   - Before pushing major header/footer or CSS changes, run relevant Python utility scripts in `utility/` to keep components in sync across pages.

---

## Project Roadmap (Key Items)

- Fix hard-coded system paths in `utility/` scripts.
- Establish `requirements.txt` and `README.md`.
- Streamline site build / GitHub Actions workflow configuration.
- Implement configuration file for global properties (e.g., Analytics ID).
