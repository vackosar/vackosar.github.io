---
layout: post
title: "Quilt - data versioning tips TODO"
date: 2021-07-01
categories: ml
description: TODO
permalink: /:categories/:title
redirect_from:
- /ml/PID-controller
---

{% include mathjax.html %}
{% include load_video.html %}

## Versioning Data from Python
[Quilt](https://quiltdata.com/) allows you to version individual files as well as entire folders inside "packages" using Python methods and AWS S3 storage.
For example, you can use it to version a single CSV dataset file, or a folder containing model files.
The files and their versioning information lives in AWS's cloud storage S3.
Specific package versions are references via `top_hash` parameter which represents hash of all files that are part of the package.


## Example
You can try Quilt for yourself following instructions in this section.

1. Install Quilt: ``` pip install quilt3 ```
2. Create your S3 bucket e.g. `my-quilt-test`.
3. Turn on S3 versioning (see [Quilt Uses S3 Versioning](#quilt-uses-s3-versioning))

Let say we have a local folder where we'd like to store local copies, s3 bucket, and a single file to version.
```python
LOCAL_FOLDER = './quilt_test/'
S3_BUCKET = 'my-quilt-test'
FILENAME = 'file1.csv'
```

Unit of storage in Quilt is a package.
Each package has a name.
Unfortunately the allowed package names are quite limited.
Each name has to be two alphanumeric strings separated by a slash.

```
PKG_NAME = 'test/quilt_test'
```
So let's create some testing dataset CSV using Pandas.
Pass set it into a Quilt package.
```
pd.DataFrame(dict(col1=[0, 1, 2]).to_csv(LOCAL_FOLDER + FILENAME)
p = quilt3.Package()
p.set(FILENAME, LOCAL_FOLDER + FILENAME)
```

And push it to the remote S3. After that, let's store the package hash.

```
p.push(PKG_NAME)
HASH = p.top_hash
```

Now we can download the data referring to their specific hash version via `top_hash`.

```
quilt3.Package.install(PKG_NAME, registry=S3_BUCKET, top_hash=HASH, dest=LOCAL_FOLDER)
```

If you already have the same version on local machine,
Quilt doesn't seem to download the files again.
It doesn't tell you that directly, in default logging setup.
Only the download speed is unrealistically fast.


## Quilt Uses S3 Versioning

When didn't have [S3 versioning enabled my bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html), Quilt versioning silently failed.
It was downloading the latest versions of all files regardless of the hash without warning.
I also haven't found any good documentation on this on Quilt website.
To enable S3 versioning later, I had to clear my local cache like so:

```bash
  rm -r ~/.cache/Quilt
  rm -r ~/.local/share/Quilt/packages/.quilt 
```

## Verdict

Apart from the initial versioning hick-up, Quilt data works pretty well.
Good luck and see you next time!