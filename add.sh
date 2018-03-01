#!/bin/sh
set -xue

title="$1"
link="$2"
now="$(date +%F)"
file="_posts/$now-$(echo "$title" | sed 's/ /-/g').md"

#if echo "$text" |grep -q "http"; then
#    link="$text"
#    text="[$text]($text)"
#fi

echo "---
layout: post
title: \"$title\"
date: $now
---
[$link]($link)
<script language=\"javascript\">
    window.location.href = \"$link\"
</script>
"
> "$file"

git add "$file"
git commit -m "$title"
echo "Please push"
