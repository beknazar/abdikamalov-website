# Professor Bakhtiyar Abdikamalov - Academic Website

This repository hosts the personal website of Professor Bakhtiyar Abdikamalov, featuring academic works, publications, and resources in physics and Karakalpak literature.

## 🌐 Website URLs

- **Main Website:** https://abdikamalov.com
- **Modern Version:** https://abdikamalov.com/new
- **GitHub Pages:** https://beknazar.github.io/abdikamalov-website/

## 📁 Project Structure

```
├── index.htm              # Classic version (original design)
├── new/                   # Modern multilingual version
│   └── index.html        # Responsive design with EN/RU/KAA support
├── files/                 # Academic documents (PDFs, DJVU, etc.)
├── sh/                    # Poetry collection (HTML files)
├── scripts/               # Utility scripts
│   ├── download_main_files.py    # Download files from files.json
│   ├── download_sh_files.py      # Download sh/ content
│   ├── update_links.py           # Update narod.ru links
│   ├── fix_links.py              # Fix file paths
│   └── check_missing_files.py    # Check for missing files
├── abdikamalov_profile.jpg       # Profile image
├── files.json             # Main files manifest
├── sh_files.json          # Poetry files manifest
└── DNS_SETUP.md          # DNS configuration guide
```

## 🚀 Features

### Classic Version (index.htm)
- Original design preserving the historical layout
- Complete academic works collection
- Links to physics textbooks, Karakalpak literature, and cultural materials

### Modern Version (/new)
- **Responsive Design** - Works on all devices
- **Multilingual Support** - English, Russian, and Karakalpak (Cyrillic)
- **Search Functionality** - Find content across all categories
- **Organized Categories**:
  - Karakalpak Literature
  - Physics Textbooks
  - Scientific Articles
  - Educational Materials
  - Translations
  - Cultural Heritage

## 🛠️ Local Development

### Download Content Files

1. Download main academic files:
```bash
python3 scripts/download_main_files.py
```

2. Download poetry collection:
```bash
python3 scripts/download_sh_files.py
```

### Update Links
To migrate from narod.ru to abdikamalov.com:
```bash
python3 scripts/update_links.py
```

## 🌍 Custom Domain Setup

The website uses a custom domain (abdikamalov.com) with GitHub Pages. See `DNS_SETUP.md` for configuration details.

## 📝 Content

- **245+ Academic Files** - Physics textbooks, research papers, educational materials
- **147 Poetry Files** - Karakalpak poetry collection in the sh/ directory
- **Translations** - Major physics works translated to Karakalpak by Prof. Abdikamalov
- **Cultural Heritage** - Karakalpak music and literary works

## 🔄 Migration from Narod.ru

This website has been migrated from `abdikamalov.narod.ru` to `abdikamalov.com`. All content is preserved and links have been updated.

## 📄 License

All content belongs to the respective authors and is shared for educational purposes.