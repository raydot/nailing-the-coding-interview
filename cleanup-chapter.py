#!/usr/bin/env python3
"""
Automated cleanup script for converted Markdown chapters.
Handles common conversion artifacts and formatting issues.
"""

import re
import sys
from pathlib import Path

def clean_chapter(file_path):
    """Clean up a single chapter file."""
    print(f"Cleaning: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    changes = []
    
    # 1. Convert HTML sidebars to Markdown blockquotes
    def convert_sidebar(match):
        title = match.group(1) if match.group(1) else "Note"
        body = match.group(2).strip()
        # Convert to blockquote
        lines = body.split('\n')
        quoted = '\n'.join(f'> {line}' if line.strip() else '>' for line in lines)
        return f'> **{title}**\n>\n{quoted}'
    
    # Match sidebar pattern
    sidebar_pattern = r'<div class="sidebar">\s*(?:<div class="title">\s*(.*?)\s*</div>\s*)?(.*?)</div>'
    new_content = re.sub(sidebar_pattern, convert_sidebar, content, flags=re.DOTALL)
    if new_content != content:
        changes.append("Converted HTML sidebars to Markdown blockquotes")
        content = new_content
    
    # 2. Remove standalone closing divs
    content_before = content
    content = re.sub(r'^\s*</div>\s*$', '', content, flags=re.MULTILINE)
    if content != content_before:
        changes.append("Removed standalone closing div tags")
    
    # 3. Fix code blocks - add python as default language for code without language
    # This is conservative - only fixes obvious Python code
    def fix_code_block(match):
        code = match.group(1)
        # Check if it looks like Python
        if any(keyword in code for keyword in ['def ', 'import ', 'class ', 'print(', 'return ', 'if __name__']):
            return f'```python\n{code}\n```'
        # Check if it looks like JavaScript
        elif any(keyword in code for keyword in ['function ', 'const ', 'let ', 'var ', '=>', 'console.log']):
            return f'```javascript\n{code}\n```'
        # Check if it looks like Java
        elif any(keyword in code for keyword in ['public class', 'public static', 'System.out']):
            return f'```java\n{code}\n```'
        # Leave as-is if unsure
        return match.group(0)
    
    code_pattern = r'```\n(.*?)\n```'
    new_content = re.sub(code_pattern, fix_code_block, content, flags=re.DOTALL)
    if new_content != content:
        changes.append("Added language tags to code blocks")
        content = new_content
    
    # 4. Convert note/tip/warning callouts
    callout_pattern = r'\[!(NOTE|TIP|WARNING|IMPORTANT)\]\s*\n(.*?)(?=\n\n|\n>|\Z)'
    def convert_callout(match):
        callout_type = match.group(1)
        text = match.group(2).strip()
        icon = {
            'NOTE': '📝',
            'TIP': '💡',
            'WARNING': '⚠️',
            'IMPORTANT': '❗'
        }.get(callout_type, '📌')
        return f'> {icon} **{callout_type}**\n>\n> {text}'
    
    new_content = re.sub(callout_pattern, convert_callout, content, flags=re.DOTALL | re.MULTILINE)
    if new_content != content:
        changes.append("Converted callout boxes")
        content = new_content
    
    # 5. Fix common formatting issues
    # Remove excessive blank lines (more than 2 in a row)
    content = re.sub(r'\n{4,}', '\n\n\n', content)
    
    # 6. Fix list formatting (ensure blank line before lists)
    content = re.sub(r'([^\n])\n(\d+\.\s)', r'\1\n\n\2', content)
    content = re.sub(r'([^\n])\n(-\s)', r'\1\n\n\2', content)
    
    # Write back if changed
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✓ Changes made:")
        for change in changes:
            print(f"    - {change}")
        return True
    else:
        print(f"  → No changes needed")
        return False

def main():
    if len(sys.argv) < 2:
        print("Usage: python cleanup-chapter.py <chapter-file> [chapter-file...]")
        print("   or: python cleanup-chapter.py all")
        sys.exit(1)
    
    if sys.argv[1] == 'all':
        chapters_dir = Path('chapters')
        files = sorted(chapters_dir.glob('*.md'))
    else:
        files = [Path(f) for f in sys.argv[1:]]
    
    total = len(files)
    changed = 0
    
    print(f"Processing {total} file(s)...\n")
    
    for file_path in files:
        if clean_chapter(file_path):
            changed += 1
        print()
    
    print(f"Summary: {changed}/{total} files modified")

if __name__ == '__main__':
    main()
