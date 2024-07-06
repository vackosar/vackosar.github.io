---
title: Bash Tricks I Use
description: Error handling, star expansion, exporting variables from an env file.
categories: software
date: 2024-06-09
last_modified_at: 2024-06-09
layout: post
permalink: /:categories/:title
my_related_post_paths:
- _posts/2016-07-28-Functional-Foreach-In-Bash.md
- _posts/2017-06-04-Code-Structure-Principles.md
- _posts/2024-01-24-How-To-Install-Your-Python-Version-On-Ubuntu.md
- _posts/2022-02-06-twitter-bullet-points-to-copy-paste.md
- _posts/2018-09-23-Debounce-In-Bash-To-Fix-Lenovo-Touchpad-And-Trackpoint-Lost-Sync.md
- _posts/2020-04-08-Python-Context-Manager-With-Statement-Exception-Handling.md
- _posts/2023-01-24-fill-versions-from-python-environment.md
---

{% include highlight-rouge-friendly.css.html %}


Avoid bash if you can and use for example python.
Reason is that the bash scripts cannot grow into a larger program, because debugging and crazy syntax.

But sometimes you will encounter bash.


## Error Handling with Or Operator "||"

```
# I usually set these options.
# The -e option causes bash to exit immediately if any command exits with a non-zero status.
# The -x option prints every command before it is executed to simulate debugging.
# The -u option causes bash to exit immediately if any unset variable is used.

set -eux

echo "before";
{
  echo "inner";
  
  # This will cause exit from the function.
  false;
  
  echo "we will never get here";
  
} || echo failed

echo "continue here";

# This will cause exit.
false;

echo "We will never get here :(";
```


## Careful with the Star Expansion!

Remember `.*` expands also to `..`, which is outer directory!


## Listen to The Output of an Already Running Process
The process needs not to have its output piped to a file or other pipe. 
You can access the output via the proc filesystem:

```cat /proc/<pid>/fd/1```.

Example:
```
echo "while true; do sleep 1;   echo here; done;" > test.sh;
nohup bash test.sh &
# prints: [1] 1020383
cat /proc/1020383/fd/1;
```

For stderr use `2` instead of `1`:
```
cat /proc/<pid>/fd/2
```

Because:
- 0: stdin
- 1: stdout
- 2: stderr


## How to Export All Variables From an Env File

Avoid manual exporting with `allexport` option.
All variables that will be newly defined variables will be exported for use in executed commands. 

Example:
```
set -o allexport

source .env
set +o allexport
```


## Other Sources

- TODO 

Good luck!