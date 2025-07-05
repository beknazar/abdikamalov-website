#!/usr/bin/env python3
import json
import os
import requests
import hashlib
import time
from urllib.parse import quote

BASE_URL = "https://abdikamalov.narod.ru/abdikamalov/"
FILES_DIR = "files"
PROGRESS_FILE = "download_progress.txt"
CHUNK_SIZE = 8192

def get_downloaded_files():
    """Read the list of already downloaded files"""
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, 'r') as f:
            return set(line.strip() for line in f if line.strip())
    return set()

def add_to_downloaded(filename):
    """Add a file to the downloaded list"""
    with open(PROGRESS_FILE, 'a') as f:
        f.write(filename + '\n')

def download_file(filename, expected_size=None):
    """Download a single file with resume capability"""
    filepath = os.path.join(FILES_DIR, filename)
    url = BASE_URL + quote(filename)
    
    headers = {}
    mode = 'wb'
    resume_pos = 0
    
    # Check if partial file exists
    if os.path.exists(filepath):
        resume_pos = os.path.getsize(filepath)
        if expected_size and resume_pos >= expected_size:
            print(f"✓ {filename} already complete ({resume_pos} bytes)")
            return True
        headers['Range'] = f'bytes={resume_pos}-'
        mode = 'ab'
        print(f"↻ Resuming {filename} from {resume_pos} bytes")
    else:
        print(f"↓ Downloading {filename}")
    
    try:
        response = requests.get(url, headers=headers, stream=True, timeout=30)
        response.raise_for_status()
        
        total_size = int(response.headers.get('content-length', 0))
        if resume_pos > 0:
            total_size += resume_pos
        
        with open(filepath, mode) as f:
            downloaded = resume_pos
            for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
                if chunk:
                    f.write(chunk)
                    downloaded += len(chunk)
                    # Progress indicator
                    if total_size > 0:
                        percent = (downloaded / total_size) * 100
                        print(f"\r  {percent:.1f}% ({downloaded}/{total_size} bytes)", end='', flush=True)
        
        print()  # New line after progress
        return True
        
    except requests.exceptions.RequestException as e:
        print(f"✗ Error downloading {filename}: {e}")
        return False
    except KeyboardInterrupt:
        print(f"\n⚠ Download interrupted for {filename}")
        raise

def main():
    # Create files directory if it doesn't exist
    if not os.path.exists(FILES_DIR):
        os.makedirs(FILES_DIR)
        print(f"Created directory: {FILES_DIR}")
    
    # Load files.json
    try:
        with open('files.json', 'r') as f:
            files_data = json.load(f)
    except FileNotFoundError:
        print("Error: files.json not found")
        return
    except json.JSONDecodeError:
        print("Error: Invalid JSON in files.json")
        return
    
    # Get already downloaded files
    downloaded = get_downloaded_files()
    
    total_files = len(files_data)
    downloaded_count = 0
    failed_files = []
    
    print(f"Total files to download: {total_files}")
    print(f"Already downloaded: {len(downloaded)}")
    print("-" * 50)
    
    try:
        for i, file_info in enumerate(files_data, 1):
            filename = file_info.get('name', '')
            if not filename:
                print(f"⚠ Skipping entry {i}: no filename")
                continue
            
            print(f"\n[{i}/{total_files}] {filename}")
            
            # Skip if already downloaded
            if filename in downloaded:
                print(f"✓ Already downloaded")
                downloaded_count += 1
                continue
            
            # Download the file
            expected_size = file_info.get('size')
            if download_file(filename, expected_size):
                add_to_downloaded(filename)
                downloaded_count += 1
            else:
                failed_files.append(filename)
            
            # Small delay to be respectful to the server
            time.sleep(0.5)
    
    except KeyboardInterrupt:
        print("\n\n⚠ Download interrupted by user")
    
    # Summary
    print("\n" + "=" * 50)
    print(f"Download Summary:")
    print(f"  Total files: {total_files}")
    print(f"  Downloaded: {downloaded_count}")
    print(f"  Failed: {len(failed_files)}")
    
    if failed_files:
        print(f"\nFailed files:")
        for f in failed_files:
            print(f"  - {f}")
        print("\nRun the script again to retry failed downloads")

if __name__ == "__main__":
    main()