#!/usr/bin/env python3
import re
import os

def update_links_in_file(filepath, is_new_version=False):
    """Update all narod.ru links to use the new domain"""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Replace various narod.ru URL patterns
    replacements = [
        # Full URLs to files in the main directory
        (r'https?://(?:www\.)?abdikamalov\.narod\.ru/abdikamalov/([^"\'>\s]+)', r'https://abdikamalov.com/files/\1'),
        (r'https?://(?:www\.)?abdikamalov\.narod\.ru/([^/][^"\'>\s]+)', r'https://abdikamalov.com/files/\1'),
        
        # URLs to sh/ directory files
        (r'https?://(?:www\.)?abdikamalov\.narod\.ru/sh/([^"\'>\s]+)', r'https://abdikamalov.com/sh/\1'),
        
        # Just domain references
        (r'https?://(?:www\.)?abdikamalov\.narod\.ru/?(?=["\'>])', r'https://abdikamalov.com'),
        
        # Any remaining narod.ru references (without protocol)
        (r'(?:www\.)?abdikamalov\.narod\.ru/abdikamalov/([^"\'>\s]+)', r'abdikamalov.com/files/\1'),
        (r'(?:www\.)?abdikamalov\.narod\.ru/sh/([^"\'>\s]+)', r'abdikamalov.com/sh/\1'),
        (r'(?:www\.)?abdikamalov\.narod\.ru/?(?=["\'>])', r'abdikamalov.com'),
    ]
    
    for pattern, replacement in replacements:
        content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)
    
    # For the new version, update relative paths to files
    if is_new_version:
        # Update relative paths in new/index.html to go up one directory
        content = re.sub(r'href="files/', r'href="../files/', content)
        content = re.sub(r'href="sh/', r'href="../sh/', content)
        content = re.sub(r'src="files/', r'src="../files/', content)
        content = re.sub(r'src="sh/', r'src="../sh/', content)
        
        # Fix any double ../.. that might have been created
        content = re.sub(r'href="\.\./\.\./files/', r'href="../files/', content)
        content = re.sub(r'href="\.\./\.\./sh/', r'href="../sh/', content)
        content = re.sub(r'src="\.\./\.\./files/', r'src="../files/', content)
        content = re.sub(r'src="\.\./\.\./sh/', r'src="../sh/', content)
    
    # Update jQuery to latest CDN (3.7.1 as of 2024)
    jquery_replacements = [
        # Replace old jQuery versions
        (r'<script[^>]*src="[^"]*jquery[^"]*\.js"[^>]*></script>', 
         '<script src="https://cdn.jsdelivr.net/npm/jquery@3.7.1/dist/jquery.min.js"></script>'),
        
        # Replace jQuery UI if present
        (r'<script[^>]*src="[^"]*jquery-ui[^"]*\.js"[^>]*></script>', 
         '<script src="https://cdn.jsdelivr.net/npm/jquery-ui@1.13.2/dist/jquery-ui.min.js"></script>'),
        
        # Update any narod.ru hosted scripts
        (r'<script[^>]*src="[^"]*narod\.ru[^"]*\.js"[^>]*></script>', ''),
    ]
    
    for pattern, replacement in jquery_replacements:
        content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)
    
    # Remove any empty script tags
    content = re.sub(r'<script[^>]*>\s*</script>\s*\n?', '', content)
    
    # Count changes
    changes = 0
    if content != original_content:
        changes = len([m for pattern, _ in replacements + jquery_replacements 
                      for m in re.finditer(pattern, original_content, re.IGNORECASE)])
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
    
    return changes

def main():
    print("Updating links in website files...")
    print("=" * 50)
    
    # Update index.htm
    if os.path.exists('index.htm'):
        changes = update_links_in_file('index.htm', is_new_version=False)
        print(f"✓ Updated index.htm - {changes} changes made")
    else:
        print("✗ index.htm not found")
    
    # Update new/index.html
    if os.path.exists('new/index.html'):
        changes = update_links_in_file('new/index.html', is_new_version=True)
        print(f"✓ Updated new/index.html - {changes} changes made")
    else:
        print("✗ new/index.html not found")
    
    print("\n" + "=" * 50)
    print("Link update complete!")
    print("\nAll narod.ru links have been updated to abdikamalov.com")
    print("jQuery has been updated to latest CDN version (3.7.1)")
    
    # Show example transformations
    print("\nExample transformations:")
    print("  http://www.abdikamalov.narod.ru/abdikamalov/file.pdf")
    print("  → https://abdikamalov.com/files/file.pdf")
    print("\n  http://www.abdikamalov.narod.ru/sh/140.html")
    print("  → https://abdikamalov.com/sh/140.html")

if __name__ == "__main__":
    main()