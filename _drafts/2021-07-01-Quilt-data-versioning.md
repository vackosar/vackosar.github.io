---
layout: post
title: "Quilt - data versioning tips TODO"
date: 2021-07-01
categories: ml
description: TODO
permalink: /:categories/:title
video: PHIKbgMJq4c
image: /images/wav2vec-thumb.png
redirect_from:
- /ml/PID-controller
---

{% include mathjax.html %}
{% include load_video.html %}

## Versioning Data from Python
[Quilt](https://quiltdata.com/) allows you to version files and folders using Python methods.
You can use it to version a single CSV file, or a folder containing model files.
The versioning information is stored in cloud file storage like S3.
How can you refer to the specific version of the data?
You use `top_hash` value which represents hash of all files that are part of the package.


## Example
You can try Quilt for yourself following instructions in this section.
Don't forget to turn on S3 versioning

1. Install Quilt: ``` pip install quilt3 ```
2. Create your S3 bucket e.g. `my-quilt-test`.
3. Turn on S3 versioning (see [Quilt Uses S3 Versioning](#quilt-uses-s3-versioning))

Let say we have a local folder where we'd like to store local copies, s3 bucket and a single file to version.
```python
LOCAL_FOLDER = './quilt_test/'
S3_BUCKET = 'my-quilt-test'
FILENAME = 'file1.csv'
```

Files are stored in Quilt in named packages.
Unfortunately the allowed package names are quite limited.
You have to have exactly one slach in the name and use liit

```
PKG_NAME = 'test/quilt_test'
```

```
pd.DataFrame(dict(col1=[0, 1, 2]).to_csv(LOCAL_FOLDER + FILENAME)

p = quilt3.Package()
p.set(FILENAME, LOCAL_FOLDER + FILENAME)
```

```
p.push(PKG_NAME)
```


```
quilt3.Package.install(PKG_NAME, registry=quilt_s3_bucket, top_hash=HASH, dest=result_path)
```

# Quilt Uses S3 Versioning

If you don't turn this on, Quilt versioning will mostly silently fail for you.
In some cases, it was downloading the latest versions of all files with no warning.
If you turn on S3 versioning later, you'll need to clear your local cache to get the versioning working again.

```bash
  rm -r ~/.cache/Quilt
  rm -r ~/.local/share/Quilt/packages/.quilt 
```


# Naming limitation
- issues: package name limitations


