---
title: Fill Versions From Python Environment
description: Script that fills in versions into your requirements file
categories: software
date: 2023-01-24
last_modified_at: 2023-01-24
image: /images/fill-versions-from-python-environment.png
layout: post
permalink: /:categories/:title
my_related_post_paths:
- _posts/2016-07-03-GitFlow-Incremental-Builder.md
- _posts/2020-04-08-Python-Context-Manager-With-Statement-Exception-Handling.md
- _posts/2016-07-22-Obsolete-Branch-Remover.md
- _posts/2018-01-24-Modern-Config-Injection-In-Maven-Plugins.md
- _posts/2022-08-03-Python-functools.cmp_to_key-explained.md
- _posts/2018-10-04-Spline-Data-Lineage-Spark-Structured-Streaming-Spark-AI-Summit-2018.md
---

{% include highlight-rouge-friendly.css.html %}

Would you like to have **all versions set into your requirements.txt?**
Perhaps you don't want the full version pinning of all dependencies, but just would like the top package versions locked?
All the PyPi **package versions are already in your virtual environment**, and you don't want to have to **fill them in** manually?

Use the **Python script below** to write your fancy new file into **requirements_new.txt for review**. All your comments will be preserved. 
If you have any issues or suggestions, let me know. Enjoy, its Apache 2 licenced.

```python
#!/bin/python

"""
A script that reads pip freeze, and fills in missing versions into requirements.txt for corresponding packages.
If the version in requirements.txt does not match print a warning. Ignore comments in requirement.txt.
"""

import re
import subprocess

# Get the output of pip freeze
pip_freeze = subprocess.run(["pip", "freeze"], capture_output=True, text=True)
pip_freeze_output = pip_freeze.stdout

# Read the contents of requirements.txt
with open("requirements.txt", "r") as f:
    requirements_txt = f.read()

# Split the output of pip freeze into individual packages
pip_freeze_lines = pip_freeze_output.split("\n")
pip_freeze_packages = {}
for line in pip_freeze_lines:
    # Ignore empty lines
    if line == "":
        continue

    # Split the line into package name and version
    package, version = line.split("==")
    pip_freeze_packages[package] = version

# Split the contents of requirements.txt into individual packages
requirements_txt_lines = requirements_txt.split("\n")
requirements_txt_packages = {}
requirements_txt_lines_result = []
for line in requirements_txt_lines:
    # Ignore empty lines
    if line.strip() == "" or line.strip().startswith("#"):
        requirements_txt_lines_result.append(line)

    elif '==' not in line:
        requirements_txt_packages[line] = None
        version = pip_freeze_packages.get(line)
        if version is None:
            print(f'WARNING: Requirement {line} not installed!')

        else:
            requirements_txt_lines_result.append(line + '==' + version)

    else:
        # Split the line into package name and version
        package, version = line.split("==")
        freeze_version = pip_freeze_packages.get(package)
        if version != freeze_version:
            print(f'WARNING: Requirement {line} does not match installed version: {freeze_version}')

        requirements_txt_lines_result.append(line)
        requirements_txt_packages[package] = version

# Update the versions in requirements.txt
with open("requirements_new.txt", "w") as f:
    for line in requirements_txt_lines_result:
        f.write(f"{line}\n")
```