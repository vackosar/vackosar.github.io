#!/bin/bash

# Loop through all .md files in the current directory and its subdirectories
find . -type f -name "*.md" | while read -r file; do
  # Use sed to perform the substitution
  sed -i.bak -E 's|!\[(.*)\]\((/images/.*)\)|{% include image.html src="\2" alt="\1" %}|g' "$file"

  sed -i.bak -E 's|<img alt="([^"]*)" style="([^"]*)" src="([^"]*)">|{% include image.html alt="\1" style="\2" src="\3" %}|g' "$file"

  sed -i.bak -E 's|<img src="([^"]*)" alt="([^"]*)" style="([^"]*)">|{% include image.html alt="\1" style="\2" src="\3" %}|g' "$file"

  # Optional: remove backup files if you are confident the replacement is correct
  rm -- "${file}.bak"
done