# Next Steps: Content Cleanup

## ✅ Phase 1 Complete: Initial Conversion

All 16 chapters have been converted from AsciiDoc to Markdown!

- ✅ Preface + 15 chapters converted
- ✅ Original files preserved in `asciidoc-source/`
- ✅ Jupyter Book builds successfully
- ✅ All committed to git

## 🎯 Phase 2: Content Cleanup (Current Phase)

Now we need to clean up the converted Markdown files. Here's what needs attention:

### 1. Remove O'Reilly Branding

**In Preface (chapters/00-preface.md):**
- [ ] Remove O'Reilly contact information
- [ ] Remove "O'Reilly Online Learning" section
- [ ] Remove O'Reilly code download links
- [ ] Update "How to Contact Us" with your own info
- [ ] Remove O'Reilly copyright notices

**Check all chapters for:**
- [ ] O'Reilly references in text
- [ ] O'Reilly URLs
- [ ] O'Reilly trademarks

### 2. Fix Code Blocks

Many code blocks may need language tags fixed:

```markdown
# Before (no language)
```
code here
```

# After (with language)
```python
code here
```
```

**Common languages in your book:**
- `python`
- `javascript`
- `java`
- `c`
- `bash`

### 3. Fix Formatting Issues

**Sidebars/Callouts:**
- Convert `<div class="sidebar">` to Markdown blockquotes
- Format: `> **Title**\n> \n> Content`

**Tables:**
- Verify all tables render correctly
- Fix any broken table formatting

**Lists:**
- Check numbered and bulleted lists
- Fix any nesting issues

**Math notation:**
- Ensure LaTeX math renders: `$inline$` and `$$block$$`

### 4. Images

**Current status:** Most images are marked "TK" (to come)

**Options:**
1. Create missing diagrams
2. Remove placeholder references
3. Find/create replacement images

**If keeping images:**
- Move to `images/` directory
- Update paths in Markdown
- Organize by chapter: `images/chapter-01/diagram.png`

### 5. Cross-References

Update internal links between chapters:
- Old: `<<DtCI_ch02>>`
- New: `[Chapter 2](02-big-o.md)`

### 6. Code Examples

**Existing code directory:** `code/`

**Tasks:**
- [ ] Verify all code examples still work
- [ ] Consider converting some to Jupyter notebooks
- [ ] Link from chapters to code files
- [ ] Test all code examples

## 🔧 Recommended Workflow

### Quick Wins (Do First)

1. **Remove O'Reilly content from preface**
   ```bash
   # Edit chapters/00-preface.md
   # Remove sections 268-293 (O'Reilly specific)
   ```

2. **Fix obvious code block issues**
   - Search for: ` ``` ` (triple backticks with no language)
   - Add appropriate language tags

3. **Convert sidebars**
   - Search for: `<div class="sidebar">`
   - Replace with Markdown blockquotes

### Systematic Cleanup (Chapter by Chapter)

For each chapter:
1. Open in editor
2. Run through cleanup checklist
3. Build book and preview
4. Commit changes

**Suggested order:**
- Start with Chapter 1 (shortest, good test case)
- Then Preface (remove O'Reilly content)
- Then remaining chapters

## 📝 Cleanup Checklist Template

Copy this for each chapter:

```markdown
## Chapter X: [Title]

- [ ] Remove O'Reilly references
- [ ] Fix code block language tags
- [ ] Convert sidebars to blockquotes
- [ ] Fix tables
- [ ] Update image paths
- [ ] Fix cross-references
- [ ] Test code examples
- [ ] Build and preview
- [ ] Commit
```

## 🚀 After Cleanup

Once content is cleaned up:

1. **Phase 3: Interactive Content**
   - Create Jupyter notebooks for key examples
   - Add executable code cells
   - Link notebooks from chapters

2. **Phase 4: Polish**
   - Add missing images/diagrams
   - Improve formatting
   - Add exercises/practice problems

3. **Phase 5: Deployment**
   - Set up GitHub Actions
   - Deploy to GitHub Pages
   - Configure custom domain (optional)

## 🛠️ Useful Commands

```bash
# Activate environment
conda activate coding-interview-book

# Build book
jupyter-book build .

# Preview
open _build/html/index.html

# Clean build
jupyter-book clean .

# Search for patterns
grep -r "O'Reilly" chapters/
grep -r "```$" chapters/  # Find code blocks without language
grep -r "<div" chapters/  # Find HTML divs
```

## 📊 Progress Tracking

Update this as you go:

**Chapters cleaned:** 0/16
**O'Reilly content removed:** ⏳
**Code blocks fixed:** ⏳
**Sidebars converted:** ⏳
**Images updated:** ⏳

---

**Start here:** Edit `chapters/00-preface.md` to remove O'Reilly content!
