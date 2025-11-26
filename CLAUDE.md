# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a technical book called "Nailing the Coding Interview" - a comprehensive guide to mastering technical coding interviews. The book covers data structures, algorithms, and problem-solving strategies. It is built using MyST Markdown and deployed as a static website to GitHub Pages.

**Live site:** https://codinginterviewsbook.davekanter.com/
**Repository:** https://github.com/raydot/nailing-the-coding-interview

**Book Goals:**

- Help readers create targeted study plans for interview success
- Familiarize them with common coding interview problems and strategies
- Provide real-world questions with detailed solutions
- Build understanding of essential concepts and how to apply them under pressure
- Teach both technical skills and interview communication strategies

## Build System

This project uses **MyST Markdown v2** (mystmd), NOT Jupyter Book. While the README mentions Jupyter Book (legacy), the actual build system is MyST.

### Essential Commands

```bash
# Setup (first time only)
conda env create -f environment.yml
conda activate coding-interview-book

# Build the book locally
myst build --html

# Preview the built book
open _build/html/index.html

# Clean build (if errors occur)
rm -rf _build && myst build --html

# Deploy to production
# Automated via GitHub Actions on push to main branch
# Manual deployment: git push origin main

# View specific chapter content
cat chapters/04-arrays.md | grep -A 50 "## 🎯 Interview Pattern"

# Check for smart quotes in code blocks (breaks syntax)
grep -r "[""'']" chapters/*.md

# Find image placeholders
grep -r "IMAGE TK\|GRAPHIC TK\|image TK" chapters/

# Build and open in browser (macOS)
myst build --html && open _build/html/index.html

# Build and open in browser (Linux)
myst build --html && xdg-open _build/html/index.html
```

### Development Workflow

1. Activate conda environment: `conda activate coding-interview-book`
2. Edit content in `chapters/` directory
3. Build locally: `myst build --html`
4. Preview: `open _build/html/index.html`
5. Commit and push to trigger automatic deployment

## Project Structure

```
nailing-the-coding-interview/
├── chapters/              # Book chapters (main content)
│   ├── 00-preface.md
│   ├── 01-preparing.md
│   ├── 02-big-o.md
│   ├── part-01.md        # Part separator
│   ├── 03-strings.md
│   ├── 04-arrays.md
│   ├── 05-linked-lists.md
│   ├── 06-stacks-queues.md
│   ├── 07-heaps.md
│   ├── 08-hashes.md
│   ├── 09-trees.md
│   ├── 10-graphs.md
│   ├── part-02.md        # Part separator
│   ├── 11-functions-recursion.md
│   ├── 12-search.md
│   ├── 13-sort.md
│   ├── part-03.md        # Part separator
│   ├── 14-dynamic-greedy.md
│   ├── 15-outside-the-box.md
│   └── 16-gen-ai-to-study.md
├── images/               # Images organized by chapter (ch_02/, ch_03/, etc.)
├── code/                 # Standalone code examples for each chapter
│   ├── ch02_big0/
│   ├── ch03_strings/
│   ├── ch04_arrays/
│   └── ... (mirrors chapter structure)
├── docs/                 # Internal documentation and planning
│   ├── TASKS.md          # Current tasks and image tracking
│   ├── REFERENCE.md      # Quick reference for development
│   ├── interview-pattern-workflow.md  # Workflow for adding interview patterns
│   └── archive/          # Migration documentation
├── _build/               # Build output (gitignored)
├── myst.yml              # MyST configuration and table of contents
├── environment.yml       # Conda environment definition
├── intro.md              # Book landing page
├── README.md             # GitHub repository landing page
└── SETUP.md              # Development environment setup guide
```

## Configuration Files

- **myst.yml**: MyST configuration, defines table of contents structure and site settings
- **environment.yml**: Python dependencies (Python 3.11, mystmd, jupyterlab, numpy, matplotlib, pandas)
- **.github/workflows/deploy.yml**: GitHub Actions workflow for automatic deployment to GitHub Pages
- **docs/interview-pattern-workflow.md**: Workflow guide for adding interview patterns to chapters

## Content Architecture

### Chapter Organization

The book is structured in three parts:

1. **Introduction** (Chapters 0-2): Preparing for interviews and Big O notation
2. **Part I: Data Structures** (Chapters 3-10): Strings, arrays, linked lists, stacks, queues, heaps, hashes, trees, graphs
3. **Part II: Algorithms** (Chapters 11-13): Recursion, search, sort
4. **Part III: Advanced Topics** (Chapters 14-16): Dynamic programming, greedy algorithms, parallel thinking, using AI

Part separators are minimal Markdown files (part-01.md, part-02.md, part-03.md) that create visual divisions in the table of contents.

### Content Format

- All chapters are in MyST-flavored Markdown
- Code examples are embedded in chapters using fenced code blocks with language tags (`python, `javascript)
- Standalone code examples are in the `code/` directory, organized by chapter
- Images use relative paths: `../images/ch_XX/filename.png`

### Important Content Details

- **Code blocks**: Use proper language tags for syntax highlighting
- **Smart quotes**: Avoid smart quotes (`"` and `"`) in code blocks - use regular quotes (`"`)
- **Image placeholders**: Many chapters have "IMAGE TK" placeholders for diagrams that need to be created (tracked in docs/TASKS.md)
- **Cross-references**: Use MyST reference syntax for internal links

## Interview Pattern Enhancement (In Progress)

The book is being enhanced with "Interview Pattern" sections that demonstrate real interview communication and problem-solving approaches. This addresses a core book goal: teaching not just technical concepts, but how to communicate effectively in interviews.

### Two-Level Content Structure

Each chapter has two content types:

1. **Building Intuition**: Broad conceptual understanding of data structures/algorithms (existing content - author's established voice)
2. **Interview Patterns**: Dialog-based problem walkthroughs (new content being added) showing:
   - How to ask clarifying questions
   - How to verbalize thought process
   - Brute force → optimized progression
   - Big O analysis in context
   - Common mistakes and key insights

### Interview Pattern Format

```markdown
## 🎯 Interview Pattern: [Problem Name]

**Interviewer:** "Problem statement with constraints"

**You:** "Clarifying questions to understand requirements"

**Interviewer:** "Answers to clarifications"

**You:** "I'll start with a brute force approach to ensure I understand..."

[Brute force code with inline reasoning comments]

**You:** "This works but it's O(n²). I can optimize by..."

**Interviewer:** "What's the space complexity?"

**You:** "The optimized version uses O(n) space for..."

[Optimized code with inline reasoning comments]

> 💡 **Key Insight**
>
> The main aha moment that makes this solution work.
> Example: "Instead of searching the array (O(n)), we search a hash map (O(1))."

> ⚠️ **Common Mistake**
>
> The pitfall that candidates frequently encounter.
> Example: "Forgetting to check if complement exists before adding to map."

🔗 **Practice:** LeetCode #X (Problem Name), #Y (Related Problem)
```

### Emoji Markers (Format-Portable Tokens)

These emojis are search/replace tokens for format conversion:

- 🎯 = Interview Pattern (converts to `[PATTERN]` or `\interviewpattern{}`)
- 💡 = Key Insight (converts to `[INSIGHT]` or `\insight{}`)
- ⚠️ = Common Mistake (converts to `[MISTAKE]` or `\warning{}`)
- 🔗 = LeetCode reference (converts to `[LEETCODE]` or `\leetcode{}`)

When migrating to AsciiDoc or LaTeX, these can be converted via simple regex:

```bash
# Example conversions
sed 's/🎯/[PATTERN]/g'
sed 's/💡/[INSIGHT]/g'
sed 's/⚠️/[MISTAKE]/g'
sed 's/🔗/[LEETCODE]/g'
```

### Current Status

- **Chapter 4 (Arrays)**: Proof-of-concept chapter for interview pattern structure
  - Establishing dialog format and tone
  - Testing inline code comment style
  - Validating callout box approach
  - Defining LeetCode reference format
- **Target**: 2-3 interview patterns per chapter
- **Focus**: Problems that demonstrate reusable techniques and appear frequently in real interviews
- **Rollout**: Once Chapter 4 patterns are finalized, same structure applies to chapters 5-16

### Dialog Guidelines

- **Tone**: Professional but conversational (match Chapter 1 sample interview)
- **Progression**: Early patterns show full journey (clarifying → brute force → optimization), later patterns can be more concise
- **Realism**: Natural interview flow, no forced "aha!" moments
- **Code comments**: Show reasoning (the "why"), not just description (the "what")
- **Brevity**: Inline comments should be short - lengthy explanations go in callout boxes

## Book Voice and Style

### Target Audience

Self-taught and early-career developers preparing for technical interviews who want to understand concepts deeply, not just memorize solutions.

### Writing Principles

- **Understanding over memorization**: Teach reasoning and pattern recognition, not just solutions
- **Conversational but knowledgeable**: Professional without being dry or academic
- **Show the why**: Explain not just how algorithms work, but when and why to use them
- **Multiple approaches**: Often show brute force before optimization to teach thinking process
- **Honest about difficulty**: Don't sugarcoat hard topics; acknowledge when things are tricky
- **Build from first principles**: Construct understanding incrementally

### Tone Guidelines

- Use real-world analogies (Hot Wheels for hash tables, pancakes for stacks, grocery lines for queues)
- Address reader directly ("you")
- Show progression: "Let's start with..." → "Now let's optimize..."
- Acknowledge struggle: "This might seem confusing, but..."
- Encourage experimentation: "Try this yourself..." "Can you see why...?"
- Personal voice: Occasional personal anecdotes and teaching experiences

### Communication Focus

The book emphasizes interview communication skills as much as technical knowledge:

- How to ask clarifying questions before diving into code
- How to verbalize thinking process while solving
- How to explain trade-offs between approaches
- When and how to mention Big O complexity
- How to handle getting stuck or making mistakes

This dual focus (technical + communication) distinguishes the book from pure algorithm references.

## Known Issues & Active Work

### Chapter 4 Interview Pattern POC

Chapter 4 is being developed as the template for interview pattern integration:

- Establishing dialog format that feels natural (not forced)
- Testing inline code comment approach for showing reasoning
- Validating callout box format for insights and mistakes
- Defining LeetCode reference style
- Ensuring tone matches Chapter 1 sample interview

Once Chapter 4 patterns are complete and validated, the same structure will be systematically applied to remaining chapters (5-16).

### Missing Images (36 total)

The book has placeholders for 36 missing diagrams across chapters 4-12. These are tracked with line numbers in `docs/TASKS.md`. High-priority images include:

- Data structure diagrams (arrays, linked lists, trees, heaps, graphs)
- Algorithm visualizations (traversals, sorting, searching)
- Conceptual illustrations (Big O growth, hash collisions)

### Content Polish

- Review for smart quotes in code blocks (search for `"` and `"`)
- Some chapters need additional examples and clarifications
- Chapters 15 and 16 are incomplete and need expansion
- Space/time tradeoff concept needs verification in Chapter 2 (critical for Two Sum pattern)

### Git Status Notes

Recent work has split chapters 12 (search-sort) into separate search and sort chapters, and renumbered subsequent chapters. You may see deleted files for old chapter numbers in git status.

## Deployment

The book automatically deploys to GitHub Pages when changes are pushed to the `main` branch. The GitHub Actions workflow:

1. Sets up conda environment
2. Builds the book with `myst build --html`
3. Deploys `_build/html` to GitHub Pages

**Custom domain**: codinginterviewsbook.davekanter.com (configured in GitHub Pages settings)

**Deployment time**: Typically 2-3 minutes after push

## Code Examples

Code examples are primarily in Python, with some JavaScript examples where relevant. When adding or modifying code:

- Ensure code is correct and runnable
- Use clear variable names and comments
- Follow the language's standard style guide (PEP 8 for Python)
- Include example output or usage when helpful
- For interview patterns: Add inline comments showing reasoning, not just description

### Code Comment Guidelines for Interview Patterns

**Good inline comment (shows reasoning):**

```python
complement = target - num  # Key insight: work backwards from target
if complement in num_index:  # O(1) lookup vs O(n) array search
```

**Poor inline comment (just describes):**

```python
complement = target - num  # Calculate complement
if complement in num_index:  # Check if complement exists
```

## Common Issues and Solutions

### Build fails with "No site configuration found"

This is just a warning in MyST v2. The build should still succeed. Check `_build/html/` for output.

### Smart quotes breaking code blocks

Smart quotes (`"` `"` `'` `'`) break syntax highlighting and can cause issues.

Search for them:

```bash
grep -r "[""'']" chapters/*.md
```

Replace with regular quotes (`"` `'`) in your editor.

### Changes not showing in deployed site

- GitHub Actions takes 2-3 minutes to complete
- Check https://github.com/raydot/nailing-the-coding-interview/actions for build status
- Clear browser cache if needed (`Cmd+Shift+R` or `Ctrl+Shift+R`)
- Verify changes are in `main` branch: `git branch --show-current`

### Conda environment issues

```bash
# Remove and recreate environment
conda deactivate
conda env remove -n coding-interview-book
conda env create -f environment.yml
conda activate coding-interview-book
```

### MyST build errors

```bash
# Clean build (removes cached files)
rm -rf _build
myst build --html

# Check MyST version
myst --version  # Should be 2.0+

# Verify conda environment is activated
conda env list  # Should show * next to coding-interview-book
```

### Git merge conflicts in \_build/

The `_build/` directory is gitignored and should not cause conflicts. If it does:

```bash
# Remove _build and rebuild
rm -rf _build
git status  # Should show _build is no longer tracked
myst build --html
```

## License

This book is licensed under Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (CC BY-NC-SA 4.0).

- No commercial use
- Attribution required
- Share-alike requirement for derivatives
