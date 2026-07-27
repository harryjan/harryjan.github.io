import os

# Base directory for the repository root (evaluated relative to this file)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Google Analytics / GA4 Measurement ID
# Can be overridden by GA_MEASUREMENT_ID environment variable
GA_MEASUREMENT_ID = os.getenv("GA_MEASUREMENT_ID", "G-VE38R5Y66Q")

# Site Metadata
SITE_NAME = "Harry Jan"
SITE_URL = "https://harryjan.github.io"

# Relative paths for utility processing
WRITING_DIR = os.path.join(BASE_DIR, "writing")
CASE_STUDIES_DIR = os.path.join(BASE_DIR, "case_studies")
STYLES_DIR = os.path.join(BASE_DIR, "styles")
