#!/bin/bash
# Usage: ./process_archive.sh <archive_path> <your_id>

set -e

ARCHIVE="$1"
ID="$2"
TMPDIR="tmp_extract_$$"

# 1. Unpack archive and find the file that contains code
mkdir "$TMPDIR"
unzip -q "$ARCHIVE" -d "$TMPDIR"
CODEFILE=$(grep -rl 'CodeWord_' "$TMPDIR")

# 2. Extract the code from file
OLDCODE=$(grep -o 'CodeWord_[A-Za-z0-9]*' "$CODEFILE")

# 3. Generate a new code by adding your ID
NEWCODE="CodeWord_${ID}"

# 4. Replace the code and recreate the archive
sed -i "s/$OLDCODE/$NEWCODE/g" "$CODEFILE"
cd "$TMPDIR"
zip -qr "../${ARCHIVE%.zip}_modified.zip" .
cd ..
rm -rf "$TMPDIR"
echo "Modified archive created: ${ARCHIVE%.zip}_modified.zip"
