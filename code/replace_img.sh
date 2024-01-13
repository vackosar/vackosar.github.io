#!/bin/bash

# Loop through all .md files in the current directory and its subdirectories
find . -type f -name "*.md" | while read -r file; do
  # Use sed to perform the substitution
  sed -i.bak -E 's|!\[(.*)\]\((/images/.*)\)|{% include image.html src="\2" alt="\1" %}|g' "$file"

  # Optional: remove backup files if you are confident the replacement is correct
  rm -- "${file}.bak"
done