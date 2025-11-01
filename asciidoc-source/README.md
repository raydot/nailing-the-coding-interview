# Original AsciiDoc Source Files

This directory contains the **original AsciiDoc source files** from the O'Reilly Atlas version of the book.

## Purpose

These files are preserved as:
- **Reference** - Compare with Markdown conversions
- **Backup** - Original content is never lost
- **Source of truth** - When converting chapters to Markdown

## Do Not Edit

These files should remain **unchanged** during the migration process. All edits should be made to the Markdown versions in the `chapters/` directory.

## File Mapping

| AsciiDoc Source | Markdown Target |
|----------------|-----------------|
| preface.asciidoc | chapters/00-preface.md |
| DtCI_ch01_preparing.asciidoc | chapters/01-preparing.md |
| DtCI_ch02_big_o.asciidoc | chapters/02-big-o.md |
| DtCI_ch03_strings.asciidoc | chapters/03-strings.md |
| DtCI_ch04_arrays.asciidoc | chapters/04-arrays.md |
| DtCI_ch05_linked_lists.asciidoc | chapters/05-linked-lists.md |
| DtCI_ch06_stacks_queues.asciidoc | chapters/06-stacks-queues.md |
| DtCI_ch07_heaps.asciidoc | chapters/07-heaps.md |
| DtCI_ch08_hashes.asciidoc | chapters/08-hashes.md |
| DtCI_ch09_trees.asciidoc | chapters/09-trees.md |
| DtCI_ch10_graphs.asciidoc | chapters/10-graphs.md |
| DtCI_ch11_functions_recursion.asciidoc | chapters/11-functions-recursion.md |
| DtCI_ch12_search_sort.asciidoc | chapters/12-search-sort.md |
| DtCI_ch13_dynamic_greedy.asciidoc | chapters/13-dynamic-greedy.md |
| DtCI_ch14_outside_the_box.asciidoc | chapters/14-outside-the-box.md |
| DtCI_ch15_gen_ai_to_study.asciidoc | chapters/15-gen-ai-to-study.md |

## Conversion Workflow

1. Read AsciiDoc file from this directory
2. Convert to Markdown (using pandoc or manual conversion)
3. Clean up and edit Markdown version
4. Save to `chapters/` directory
5. Original AsciiDoc remains untouched here
