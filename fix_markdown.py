#!/usr/bin/env python3
import os
import re

files_to_fix = [
    r'c:\Users\ramba\Downloads\Job_Listing_Portal\DEPLOYMENT_GUIDE.md',
    r'c:\Users\ramba\Downloads\Job_Listing_Portal\MONGODB_SETUP.md',
    r'c:\Users\ramba\Downloads\Job_Listing_Portal\README_SETUP.md',
    r'c:\Users\ramba\Downloads\Job_Listing_Portal\SECURITY.md',
    r'c:\Users\ramba\Downloads\Job_Listing_Portal\SETUP_MONGODB_ATLAS.md'
]

for filepath in files_to_fix:
    if os.path.exists(filepath):
        print(f"Processing: {filepath}")
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_length = len(content)
        
        # Fix blank lines before headings (MD022)
        content = re.sub(r'\n(#{1,6} )', r'\n\n\1', content)
        
        # Fix blank lines around fenced code blocks (MD031)
        # Before code block
        content = re.sub(r'([^\n])\n(```)', r'\1\n\n\2', content)
        # After code block  
        content = re.sub(r'(```)\n([^\n])', r'\1\n\n\2', content)
        
        # Ensure language specified on code fences is handled
        content = re.sub(r'(^```)\s*\n', r'\1text\n', content, flags=re.MULTILINE)
        
        # Fix blank lines around lists (MD032)
        content = re.sub(r'([^\n])\n([-*+] )', r'\1\n\n\2', content)
        content = re.sub(r'([-*+] [^\n]*)\n([^\n-*+])', r'\1\n\n\2', content)
        
        # Remove trailing spaces (MD009)
        content = re.sub(r' +$', '', content, flags=re.MULTILINE)
        
        # Clean up multiple newlines to max 2
        content = re.sub(r'\n\n\n+', r'\n\n', content)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"  ✓ Fixed: {len(content)} bytes (was {original_length})")

print("\n✓ All markdown files fixed successfully!")
