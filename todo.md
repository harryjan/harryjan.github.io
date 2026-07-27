# Codebase Maintenance Roadmap

## 🚨 Must Have (High Priority & Maintenance Core)

### Fix Hard-coded Paths & Use Config
- [x] Refactor `utility/sync_headers.py` to use `BASE_DIR` from `config.py` instead of hardcoded `/Users/harryhunter/...` path
- [x] Refactor `utility/update_casestudy_css.py` to use `BASE_DIR` from `config.py`
- [x] Refactor `utility/update_article_css.py` to use `BASE_DIR` from `config.py`
- [x] Refactor `utility/update_analytics_tag.py` to use `BASE_DIR` & `GA_MEASUREMENT_ID` from `config.py`
- [x] Refactor `utility/add_analytics.py` to use `BASE_DIR` & `GA_MEASUREMENT_ID` from `config.py`
- [x] Refactor `utility/import_substack.py` to use `BASE_DIR` from `config.py`
- [x] Refactor `utility/fix_links.py` to use `BASE_DIR` from `config.py`

### Python Setup & Infrastructure
- [x] Create `requirements.txt` file listing `beautifulsoup4` and `feedparser`
- [x] Document virtual environment setup in `README.md`
- [x] Create central configuration file (`utility/config.py`)
- [x] Make analytics tracking ID configurable via environment variable or config file

### Documentation
- [x] Create `GEMINI.md` for AI/Developer context & architecture guidelines
- [x] Create `README.md` with project overview, directory structure, utility usage, and deployment guide

### GitHub Pages Workflow
- [ ] Update `.github/workflows/jekyll-gh-pages.yml` to standard static HTML deployment action (remove Jekyll build step)

---

## 💡 Nice to Have (Workflow & Content Enhancements)

### Utility Script & Content Management
- [ ] Add `--dry-run` flag to utility scripts to preview changes
- [ ] Create article template generator script (`utility/new_article.py`)
- [ ] Create case study template generator script (`utility/new_casestudy.py`)
- [ ] Add link auditing script to validate all internal relative links and images exist before deploy

### Developer Ergonomics & CSS
- [ ] Create a `Makefile` to simplify common tasks (e.g. `make sync`, `make import`)
- [ ] Standardize color palette and font declarations using CSS variables in `styles/`

---

## ✅ Completed Tasks

- [x] `GEMINI.md` project documentation created
- [x] `README.md` created
- [x] `requirements.txt` created
- [x] `utility/config.py` created
