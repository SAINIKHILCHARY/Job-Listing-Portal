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
            lines = f.readlines()
        
        fixed_lines = []
        i = 0
        
        while i < len(lines):
            line = lines[i]
            
            # Check if this line is a heading
            if re.match(r'^#{1,6} ', line):
                # Ensure blank line before heading (unless it's first line)
                if fixed_lines and fixed_lines[-1].strip() != '':
                    fixed_lines.append('\n')
                fixed_lines.append(line)
                
                # Ensure blank line after heading
                if i + 1 < len(lines) and lines[i + 1].strip() != '' and not lines[i + 1].startswith('#'):
                    fixed_lines.append('\n')
            
            # Check if this is a code fence start
            elif re.match(r'^```', line):
                # Ensure blank line before code fence
                if fixed_lines and fixed_lines[-1].strip() != '':
                    fixed_lines.append('\n')
                
                # Ensure language is specified (unless already specified or it's end fence)
                fence_match = re.match(r'^```\s*$', line)
                if fence_match and i + 1 < len(lines) and not re.match(r'^```', lines[i + 1]):
                    line = '```text\n'
                
                fixed_lines.append(line)
                
                # Look for end of code block
                if line.startswith('```') and len(line.strip()) == 3:
                    # Find closing fence
                    i += 1
                    while i < len(lines):
                        content_line = lines[i]
                        fixed_lines.append(content_line)
                        if re.match(r'^```', content_line):
                            # Ensure blank line after closing fence
                            if i + 1 < len(lines) and lines[i + 1].strip() != '':
                                if not re.match(r'^#{1,6}', lines[i + 1]):
                                    fixed_lines.append('\n')
                            break
                        i += 1
            
            # Check if this is a list item
            elif re.match(r'^[\s]*[-*+] ', line):
                # Ensure blank line before first list item
                if fixed_lines and not re.match(r'^[\s]*[-*+] ', fixed_lines[-1]) and fixed_lines[-1].strip() != '':
                    fixed_lines.append('\n')
                fixed_lines.append(line)
            
            else:
                # Remove trailing spaces from non-empty lines
                if line.strip():
                    line = line.rstrip() + '\n' if line.endswith('\n') else line.rstrip()
                
                fixed_lines.append(line)
            
            i += 1
        
        # Remove multiple consecutive blank lines (keep max 2)
        content = ''.join(fixed_lines)
        content = re.sub(r'\n\n\n+', '\n\n', content)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"  ✓ Fixed: {filepath}")

print("\n✓ All markdown files fixed successfully!")
