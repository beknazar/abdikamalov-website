#!/usr/bin/env python3
import re
import json

# Read the fixed index.htm
with open('index.htm', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract all file references
file_refs = re.findall(r'href="files/([^"]+)"', content)
file_refs = list(set(file_refs))  # Remove duplicates

# Read files.json to get available files
with open('files.json', 'r') as f:
    files_data = json.load(f)

available_files = [item['name'] for item in files_data]
available_files_lower = {f.lower(): f for f in available_files}

# Check what's missing (case-insensitive)
missing_files = []
case_mismatches = []

for ref in file_refs:
    ref_lower = ref.lower()
    if ref_lower in available_files_lower:
        if available_files_lower[ref_lower] != ref:
            case_mismatches.append((ref, available_files_lower[ref_lower]))
    else:
        # Remove the "files/" prefix if it exists
        clean_ref = ref.replace('files/', '')
        if clean_ref.lower() not in available_files_lower:
            missing_files.append(ref)

print(f"Total file references in index.htm: {len(file_refs)}")
print(f"Total files in files.json: {len(available_files)}")

if case_mismatches:
    print(f"\nFound {len(case_mismatches)} case mismatches:")
    for ref, actual in sorted(case_mismatches[:10]):
        print(f"  HTML: {ref} -> JSON: {actual}")
    if len(case_mismatches) > 10:
        print(f"  ... and {len(case_mismatches) - 10} more")

if missing_files:
    print(f"\nFound {len(missing_files)} files truly missing from files.json:")
    for f in sorted(missing_files[:20]):
        print(f"  - {f}")
    if len(missing_files) > 20:
        print(f"  ... and {len(missing_files) - 20} more")
else:
    print("\nAll referenced files exist in files.json (considering case differences)")