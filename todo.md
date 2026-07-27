# Codebase Maintenance TODO

## 🚨 Definitely Do

### Fix Hard-coded Paths
- [ ] Update `utility/sync_headers.py` line 87 - remove hard-coded path `/Users/harryhunter/Documents/1_dev_projects/my-portfolio`
- [ ] Update `utility/update_casestudy_css.py` line 52 - remove hard-coded path
- [ ] Update `utility/update_analytics_tag.py` line 51 - remove hard-coded path
- [ ] Update `utility/add_analytics.py` line 57 - remove hard-coded path
- [ ] Use `os.path.dirname(__file__)` and relative paths in all utility scripts
- [ ] Add command-line arguments to utility scripts (--root flag or similar)

### Python Dependencies
- [x] Create `requirements.txt` file listing: beautifulsoup4, feedparser
- [x] Document virtual environment setup in README

### Documentation
- [x] Create README.md with:
  - [x] Project overview
  - [x] Setup instructions (including Python dependencies)
  - [x] Usage guide for utility scripts
  - [x] Deployment instructions
  - [x] Contributing guidelines (if applicable)

### GitHub Workflow
- [ ] Remove Jekyll-specific steps from `.github/workflows/jekyll-gh-pages.yml`
- [ ] Use GitHub Pages standard publishing (simple push-to-deploy for static HTML)
- [ ] Or convert the site to a proper Jekyll setup if desired

### Configuration Management
- [x] Create a central configuration file (`utility/config.py`)
- [x] Extract analytics ID from hard-coded strings
- [x] Make analytics tracking ID configurable via environment variable or config file

---

## 💡 Nice to Have

### Utility Script Improvements
- [ ] Add `--dry-run` flag to utility scripts to preview changes
- [ ] Add backup functionality before making changes (e.g., create backups/ directory)
- [ ] Add validation to check file exists before processing
- [ ] Standardize error handling across all utility scripts
- [ ] Add logging instead of print statements for better debugging

### Content Management
- [ ] Create article template generator script
- [ ] Create case study template generator script
- [ ] Automate writing.html and case_studies.html updates when new content is added
- [ ] Add script to validate all internal links work correctly

### CSS Organization
- [ ] Audit CSS for duplicate rules
- [ ] Consider CSS variables for colors/fonts
- [ ] Organize CSS with better comments/sections
- [ ] Add CSS minification step (optional)

### Build Process
- [ ] Create a `build.sh` or `Makefile` to automate common tasks
- [ ] Add pre-commit validation (HTML/CSS linting if desired)
- [ ] Document all utility scripts and their purposes

### Error Handling & Validation
- [ ] Add basic HTML validation step before deployment
- [ ] Add link checking script to ensure no broken internal/external links
- [ ] Validate all image references exist

### Git Configuration
- [ ] Add `.gitattributes` file for consistent line endings
- [ ] Consider `.pre-commit-config.yaml` for automatic checks (optional)

---

## ✨ Perfectionist

### Static Site Generator Migration
- [ ] Consider migrating to Jekyll (since GitHub Pages workflows already configured)
- [ ] Or evaluate Hugo/11ty/Pelican for better templating
- [ ] Implement proper template inheritance for headers/footers
- [ ] Set up content collections/markdown support

### Testing
- [ ] Add unit tests for utility scripts
- [ ] Add integration tests for HTML generation
- [ ] Set up automated HTML validation in CI/CD
- [ ] Add screenshot regression testing for visual consistency

### Accessibility
- [ ] Run accessibility audit (WAVE, axe DevTools)
- [ ] Add ARIA labels where needed
- [ ] Ensure all images have meaningful alt text
- [ ] Test keyboard navigation
- [ ] Check color contrast ratios

### Performance
- [ ] Audit page load times
- [ ] Optimize image sizes (compress existing images)
- [ ] Implement lazy loading for images
- [ ] Add caching headers
- [ ] Consider image srcset for responsive images

### SEO Enhancements
- [ ] Add proper meta descriptions to all pages
- [ ] Implement Open Graph tags for social media sharing
- [ ] Add structured data (JSON-LD) for articles
- [ ] Create sitemap.xml
- [ ] Add robots.txt

### Advanced Features
- [ ] Implement search functionality for articles
- [ ] Add RSS feed generation
- [ ] Create tag/category system for articles
- [ ] Add analytics dashboard or summary
- [ ] Implement dark mode toggle
- [ ] Add reading time estimation for articles

### Security Hardening
- [ ] Add Content Security Policy (CSP) headers
- [ ] Review and minimize external script dependencies
- [ ] Add security.txt file
- [ ] Implement Subresource Integrity (SRI) for external scripts

### Developer Experience
- [ ] Set up local development server with hot reload
- [ ] Add file watchers to auto-rebuild on changes
- [ ] Create helper scripts for common authoring tasks
- [ ] Add Makefile with common commands (serve, build, deploy, test)
- [ ] Implement consistent code formatting (Black for Python, Prettier for HTML/CSS)

### Analytics & Monitoring
- [ ] Set up uptime monitoring
- [ ] Add error tracking (optional)
- [ ] Implement proper analytics event tracking
- [ ] Create analytics dashboard

### Content Management
- [ ] Add article draft/publish workflow
- [ ] Implement content scheduling
- [ ] Create admin panel for content management (optional)
- [ ] Add content versioning/history

### Polish & User Experience
- [ ] Add smooth scrolling
- [ ] Implement scroll-to-top button
- [ ] Add print stylesheet
- [ ] Optimize mobile experience further
- [ ] Add loading states for better UX
- [ ] Implement form validation (if adding contact form)

---

## Notes

- **Priority order**: Definitely Do items should be completed first as they directly impact maintainability and portability
- **Nice to Have** items can be tackled incrementally as time permits
- **Perfectionist** items are aspirational improvements that would take the site to production-grade quality
- Consider creating milestone tags in GitHub Issues for each category
- Some "Perfectionist" items may require significant architectural changes (like SSG migration)

