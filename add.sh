#!/bin/sh
set -xue

title="$1"
text="$2";
now="$(date +%F)";
file="_posts/$now-$(echo "$title" | sed 's/ /-/g').md";

echo "---
layout: post
title: \"$title\"
date: $now
---
" > "$file";


if expr match "$text" "^http" && expr match "$title" "^Link:"; then
    link="$text";
    echo "---
    layout: post
    title: \"$title\"
    date: $now
    ---
    [$link]($link)
    <script language=\"javascript\">
        window.location.href = \"$link\"
    </script>
    " >> "$file";
else
    echo "$text" >> "$file";
fi

git add "$file"
git commit -m "$title"
git push;
