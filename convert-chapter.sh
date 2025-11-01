#!/bin/bash
# Convert a single AsciiDoc chapter to Markdown
# Usage: ./convert-chapter.sh <source-file> <target-file>

set -e

SOURCE_FILE="$1"
TARGET_FILE="$2"

if [ -z "$SOURCE_FILE" ] || [ -z "$TARGET_FILE" ]; then
    echo "Usage: ./convert-chapter.sh <source-file> <target-file>"
    echo "Example: ./convert-chapter.sh asciidoc-source/DtCI_ch01_preparing.asciidoc chapters/01-preparing.md"
    exit 1
fi

if [ ! -f "$SOURCE_FILE" ]; then
    echo "Error: Source file '$SOURCE_FILE' not found"
    exit 1
fi

echo "Converting: $SOURCE_FILE → $TARGET_FILE"

# Convert using pandoc
# First convert AsciiDoc to DocBook using asciidoctor, then to Markdown
# This is a two-step process because pandoc doesn't read AsciiDoc directly

TEMP_DOCBOOK=$(mktemp).xml

echo "Step 1: Converting AsciiDoc to DocBook..."
asciidoctor -b docbook -o "$TEMP_DOCBOOK" "$SOURCE_FILE" 2>/dev/null || {
    echo "Error: asciidoctor not found. Installing..."
    gem install asciidoctor
    asciidoctor -b docbook -o "$TEMP_DOCBOOK" "$SOURCE_FILE"
}

echo "Step 2: Converting DocBook to Markdown..."
pandoc -f docbook -t gfm \
    --wrap=none \
    --extract-media=. \
    "$TEMP_DOCBOOK" -o "$TARGET_FILE"

rm "$TEMP_DOCBOOK"

echo "✓ Conversion complete!"
echo ""
echo "Next steps:"
echo "1. Review $TARGET_FILE for conversion artifacts"
echo "2. Fix code block language tags"
echo "3. Update image paths if needed"
echo "4. Remove O'Reilly-specific content"
echo "5. Test by building the book: jupyter-book build ."
