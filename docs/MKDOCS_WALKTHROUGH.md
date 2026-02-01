# MkDocs Integration Walkthrough

This document outlines the setup and customization performed to integrate MkDocs into the FAANG DSA Course project.

## 🛠 Setup Details

### 1. Dependencies
We used `uv` to manage the installation of the following tools:
- `mkdocs-material`: The core theme.
- `mkdocs-static-i18n`: For future internationalization support.
- `mkdocs-minify-plugin`: To optimize the final site output.

### 2. Configuration (`mkdocs.yml`)
The configuration is optimized for a technical course:
- **Navigation**: Organized by company (Google, Amazon, Microsoft).
- **Extensions**: Enabled Mermaid, Admonitions, and Code Highlighting.
- **Theme**: Material theme with a custom VSCode Dark Modern aesthetic.

## 🎨 Theme Customization
The "VSCode Dark Modern" look was achieved using CSS variables in `docs/stylesheets/extra.css`.

### Color Palette
| Element | Hex Color |
|---------|-----------|
| Main Background | `#1f1f1f` |
| Sidebar/Header | `#181818` |
| Primary Accent | `#007acc` |
| Code Blocks | `#1e1e1e` |

## 📂 Content Migration
- Moved `topics.md` to `docs/topics.md`.
- Updated all internal links to be relative to the `docs/` root.
- Created `docs/index.md` as the site homepage.

## ✅ Verification
The integration was verified by running `uv run mkdocs build`, ensuring a clean build with functional diagrams and links.
