set -x

title="$1"
text="$2"
now="$(date +%F)"
file="_posts/$now-$(echo "$title" | sed 's/ /-/g').md"

if echo "$text" |grep -q "http"; then
    text="[$text]($text)"
fi

echo "---
layout: post
title: \"$title\"
date: $now
---
$text" \
> "$file"

git add "$file"
git commit -m "$title"
echo "Please push"
