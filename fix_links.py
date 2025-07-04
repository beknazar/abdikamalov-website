#!/usr/bin/env python3
import re
import os

def fix_links(content):
    # Fix all PDF, DOC, DOCX, HTM links to use relative paths in files/ directory
    # Pattern to match various URL formats
    patterns = [
        # Full URLs with http/https
        (r'href="https?://[^"]*abdikamalov\.narod\.ru/abdikamalov/([^"]+\.(pdf|doc|docx|htm))"', r'href="files/\1"'),
        (r'href="https?://[^"]*abdikamalov\.narod\.ru/([^"]+\.(pdf|doc|docx|htm))"', r'href="files/\1"'),
        # Relative paths that might exist
        (r'href="([^"]+\.(pdf|doc|docx|htm))"', r'href="files/\1"'),
    ]
    
    for pattern, replacement in patterns:
        content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)
    
    # Fix image reference
    content = re.sub(r'src="https?://[^"]*abdikamalov\.narod\.ru/image004\.jpg"', 'src="abdikamalov_profile.jpg"', content)
    content = re.sub(r'src="image004\.jpg"', 'src="abdikamalov_profile.jpg"', content)
    
    # Fix common typos (being careful not to break anything)
    typo_fixes = [
        # Common Karakalpak/Russian typos
        (r'\bkarakalpk\b', 'karakalpak', re.IGNORECASE),
        (r'\bkaralpak\b', 'karakalpak', re.IGNORECASE),
        (r'\bАбдикамалов\b', 'Абдыкамалов'),  # Fix Russian spelling if needed
        (r'\bлитратура\b', 'литература', re.IGNORECASE),
        (r'\bадебият\b', 'әдебият'),  # Karakalpak spelling
        (r'\bқарақалпқ\b', 'қарақалпақ'),  # Karakalpak spelling
    ]
    
    for pattern, replacement, *flags in typo_fixes:
        flag = flags[0] if flags else 0
        content = re.sub(pattern, replacement, content, flags=flag)
    
    return content

def main():
    # Read the original file
    with open('index.htm', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix links and typos
    fixed_content = fix_links(content)
    
    # Write the fixed content
    with open('index.htm', 'w', encoding='utf-8') as f:
        f.write(fixed_content)
    
    print("Fixed all links and typos in index.htm")
    
    # Check for missing files
    print("\nChecking for missing files...")
    
    # Extract all file references
    file_refs = re.findall(r'href="files/([^"]+)"', fixed_content)
    file_refs = list(set(file_refs))  # Remove duplicates
    
    # Read files.json to get available files
    import json
    with open('files.json', 'r') as f:
        files_data = json.load(f)
    available_files = [item['name'] for item in files_data]
    
    # Check what's missing
    missing_files = []
    for ref in file_refs:
        if ref not in available_files:
            missing_files.append(ref)
    
    if missing_files:
        print(f"\nFound {len(missing_files)} files referenced but not in files.json:")
        for f in sorted(missing_files):
            print(f"  - {f}")
    else:
        print("All referenced files are available in files.json")

if __name__ == "__main__":
    main()