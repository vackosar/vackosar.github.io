---
title: Bash Tricks I Use
description: Treats for your Bash without bashing it too much!
categories: software
date: 2024-06-09
last_modified_at: 2024-06-09
layout: post
permalink: /:categories/:title
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

For stderr use `2` instead of `1`:
```
cat /proc/<pid>/fd/2
```

Because:
- 0: stdin
- 1: stdout
- 2: stderr

Other options are gdb, strace, screen: [Redirecting the Output of an Already Running Process on Linux](https://www.tutorialspoint.com/redirecting-the-output-of-an-already-running-process-on-linux)


## Avoid manual Exporting All Variables

Avoid manual exporting with `allexport` option.

Example:
```
set -o allexport

source .env
set +o allexport
```


## Other Sources

- TODO 

Good luck!