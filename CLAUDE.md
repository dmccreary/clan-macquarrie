# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an MkDocs-based documentation site for Clan MacQuarrie, an ancient Highland Scottish clan. The site focuses on educational content about the Scottish clan system and the clan's history. Built using MkDocs with the Material theme, it's deployed to GitHub Pages.

## Commands

### Build and Serve

```sh
# Build the site (outputs to site/ directory)
mkdocs build

# Run local development server at http://localhost:8000
mkdocs serve

# Deploy to GitHub Pages
mkdocs gh-deploy
```

Note: `mkdocs gh-deploy` pushes to GitHub Pages but does NOT commit source changes to Git.

### Environment Setup

This project uses Python with MkDocs Material. Set up using either conda or venv:

```sh
# Using conda (recommended if available)
conda create -n mkdocs python=3
conda activate mkdocs
pip install mkdocs "mkdocs-material[imaging]"

# Social card imaging requires additional system libraries on Mac:
brew install cairo freetype libffi libjpeg libpng zlib
export DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib
```

### Git Workflow

```sh
# Standard commit workflow
git add <files>
git commit -m "message"
git push
```

## Architecture

### Site Structure

- **mkdocs.yml**: Main configuration file defining site metadata, navigation, theme settings, and plugins
- **docs/**: All content files
  - **content/**: Organized into numbered chapter directories (01-clan-history, 02-family-history-research, etc.)
  - **img/**: Site images including logo and favicon
  - **css/**: Custom CSS styling (extra.css)
  - Root-level pages: index.md, about.md, glossary.md, references.md, contact.md, etc.

### Content Organization

Content is structured into 8 main chapters, each in a numbered directory under `docs/content/`:
1. Clan History (01-clan-histtory) - Note: contains typo in directory name
2. Family History Research (02-family-history-research)
3. Visiting Scotland (03-visit-scotland)
4. Land and Environment (04-land-and-environment)
5. Identity and Symbols (05-identity-and-symbols)
6. Education (06-education)
7. Research and Archives (07-research-and-archives)
8. Modern Activities (08-activities)

Each chapter directory contains an index.md file serving as the chapter landing page.

### Theme Configuration

Using Material theme with customizations:
- Primary color: blue, Accent: orange
- Custom logo and favicon in docs/img/
- Features enabled: code copying, navigation expansion, navigation paths, TOC following, edit action
- Edit button links to GitHub repository for community contributions

### Navigation

Navigation structure defined in mkdocs.yml maps logical page titles to file paths. When adding new content:
- Place files in appropriate chapter directory or docs root
- Update the `nav:` section in mkdocs.yml to include new pages
- Follow the existing hierarchical structure

## Important Notes

- **Directory naming**: The first content directory has a typo: `01-clan-histtory` (should be "history"). This is reflected in mkdocs.yml navigation and should be maintained for consistency unless intentionally fixed.
- **Theme**: Material theme provides extensive features. Reference [Material for MkDocs documentation](https://squidfunk.github.io/mkdocs-material/) for advanced customizations.
- **Social cards**: Social card generation (Material Social plugin) requires system-level image processing libraries and environment configuration.
- **Local testing**: Always run `mkdocs serve` to preview changes locally before deploying.
- **Deployment**: The site deploys to GitHub Pages. After running `mkdocs gh-deploy`, remember to separately commit and push source changes to the main branch.
