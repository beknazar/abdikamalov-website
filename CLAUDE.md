# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a static academic website for Professor Bakhtiyar Abdikamalov, hosted on GitHub Pages at abdikamalov.com. The project contains:
- 245+ academic documents (PDFs, DJVU files) in the `/files/` directory
- 147 poetry HTML files in the `/sh/` directory
- Two website versions: classic (index.htm) and modern (/new/index.html)
- Python utility scripts for content management in `/scripts/`

## Common Development Commands

### Content Management
```bash
# Download academic files from files.json manifest
python3 scripts/download_main_files.py

# Download poetry collection from sh_files.json
python3 scripts/download_sh_files.py

# Update old narod.ru links to abdikamalov.com
python3 scripts/update_links.py

# Verify file integrity
python3 scripts/check_missing_files.py
```

### Local Development
This is a static website - simply open HTML files in a browser:
```bash
# Classic version
open index.htm

# Modern version
open new/index.html
```

## Architecture

### Static Website Structure
- **No build process** - Pure HTML/CSS/JavaScript
- **No package.json** - No Node.js dependencies
- **No testing framework** - Static content only
- **GitHub Pages hosting** - CNAME file points to abdikamalov.com

### Content Organization
- `/files/` - Academic content organized by type (physics, literature, translations)
- `/sh/` - Poetry collection with numbered HTML files (1.html to 154.html)
- `files.json` and `sh_files.json` - Content manifests with metadata

### Key Files
- `index.htm` - Classic website preserving original design
- `new/index.html` - Modern responsive version with multilingual support (EN/RU/KAA)
- `scripts/*.py` - Utility scripts for downloading and managing content

## Important Considerations

1. **Preserve Academic Content**: All changes must maintain access to the 245+ academic files and 147 poetry files
2. **Domain Migration**: The site was migrated from abdikamalov.narod.ru - ensure all links use abdikamalov.com
3. **Static Nature**: This is a pure static site - avoid adding build tools or frameworks unless absolutely necessary
4. **GitHub Pages**: Changes pushed to main branch auto-deploy to abdikamalov.com