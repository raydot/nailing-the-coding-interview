# Conversion Workflow

## Overview

This document describes the workflow for converting chapters from AsciiDoc to Markdown while preserving the original files.

## Directory Structure

```
nailing-the-coding-interview/
├── asciidoc-source/          # ✅ ORIGINAL FILES (DO NOT EDIT)
│   ├── README.md
│   ├── preface.asciidoc
│   ├── DtCI_ch01_preparing.asciidoc
│   └── ...
├── chapters/                  # ✨ CONVERTED MARKDOWN FILES
│   ├── 00-preface.md
│   ├── 01-preparing.md (✅ CONVERTED)
│   └── ...
├── convert-chapter.sh         # Conversion script
└── _config.yml               # Jupyter Book configuration
```

## Conversion Process

### Step 1: Convert a Chapter

```bash
# Activate conda environment
conda activate coding-interview-book

# Convert a chapter
./convert-chapter.sh asciidoc-source/DtCI_ch01_preparing.asciidoc chapters/01-preparing.md
```

### Step 2: Review and Clean Up

Open the converted Markdown file and:

1. **Remove O'Reilly branding**
   - Copyright notices
   - O'Reilly contact information
   - O'Reilly Online Learning references

2. **Fix code blocks**
   - Ensure language tags are correct (python, javascript, etc.)
   - Check syntax highlighting

3. **Update images**
   - Move images to `images/` directory
   - Update image paths
   - Remove "TK" placeholders

4. **Fix formatting**
   - Convert sidebars to Markdown blockquotes
   - Fix tables
   - Update cross-references

### Step 3: Test the Build

```bash
# Build the book
jupyter-book build .

# Open in browser
open _build/html/index.html
```

### Step 4: Commit Changes

```bash
git add chapters/01-preparing.md
git commit -m "Convert Chapter 1: Preparing for the Coding Interview"
```

## Conversion Checklist

For each chapter:

- [ ] Run conversion script
- [ ] Remove O'Reilly content
- [ ] Fix code block language tags
- [ ] Update image paths
- [ ] Convert sidebars/callouts
- [ ] Fix tables
- [ ] Test chapter links
- [ ] Build and preview
- [ ] Commit to git

## Chapter Status

| Chapter | Source File | Target File | Status |
|---------|------------|-------------|--------|
| Preface | preface.asciidoc | 00-preface.md | ⏳ Not Started |
| Chapter 1 | DtCI_ch01_preparing.asciidoc | 01-preparing.md | ✅ Converted |
| Chapter 2 | DtCI_ch02_big_o.asciidoc | 02-big-o.md | ⏳ Not Started |
| Chapter 3 | DtCI_ch03_strings.asciidoc | 03-strings.md | ⏳ Not Started |
| Chapter 4 | DtCI_ch04_arrays.asciidoc | 04-arrays.md | ⏳ Not Started |
| Chapter 5 | DtCI_ch05_linked_lists.asciidoc | 05-linked-lists.md | ⏳ Not Started |
| Chapter 6 | DtCI_ch06_stacks_queues.asciidoc | 06-stacks-queues.md | ⏳ Not Started |
| Chapter 7 | DtCI_ch07_heaps.asciidoc | 07-heaps.md | ⏳ Not Started |
| Chapter 8 | DtCI_ch08_hashes.asciidoc | 08-hashes.md | ⏳ Not Started |
| Chapter 9 | DtCI_ch09_trees.asciidoc | 09-trees.md | ⏳ Not Started |
| Chapter 10 | DtCI_ch10_graphs.asciidoc | 10-graphs.md | ⏳ Not Started |
| Chapter 11 | DtCI_ch11_functions_recursion.asciidoc | 11-functions-recursion.md | ⏳ Not Started |
| Chapter 12 | DtCI_ch12_search_sort.asciidoc | 12-search-sort.md | ⏳ Not Started |
| Chapter 13 | DtCI_ch13_dynamic_greedy.asciidoc | 13-dynamic-greedy.md | ⏳ Not Started |
| Chapter 14 | DtCI_ch14_outside_the_box.asciidoc | 14-outside-the-box.md | ⏳ Not Started |
| Chapter 15 | DtCI_ch15_gen_ai_to_study.asciidoc | 15-gen-ai-to-study.md | ⏳ Not Started |

## Tools Used

- **asciidoctor** - Converts AsciiDoc to DocBook
- **pandoc** - Converts DocBook to Markdown
- **jupyter-book** - Builds the final website

## Notes

- Original AsciiDoc files in `asciidoc-source/` are **never modified**
- All edits happen in the `chapters/` directory
- Can re-convert any chapter if needed
- Conversion is a starting point - manual cleanup required
