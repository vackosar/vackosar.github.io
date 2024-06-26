---
layout: post
title: 'Spline: Data Lineage For Spark Structure Streaming (2018)'
date: 2018-10-04
last_modified_at: 2022-06-06
description: Vaclav Kosar and Marek Novotny presentation at Spark N AI Summit 2018 of a POC of Structured Streaming data lineage tool.
image: /images/2018-10-04-spark-summit-1.JPG
categories: software
permalink: /:categories/:title
video: 953PcioD6tk
slides: 31FGNIgkML7hdk
redirect_from:
- /2018/10/04/Our-Presentation-At-Spark-N-AI-Summit.html
my_related_post_paths:
- _posts/2018-12-17-My-First-Contribution-To-Major-OSS-Project.md
- _posts/2021-03-22-Automatically-Expanding-Taxonomy.md
- _posts/2021-06-21-Wav2vec2-Semi-and-Unsupervised-Speech-Recognition.md
- _posts/2019-05-18-Highly-Compressed-Richard-Hamming-Lectures.md
- _posts/2024-02-20-Synthetic-Data-for-LLM-Training.md
- _posts/2022-04-18-Understand-Large-Language-Models-like-ChatGPT.md
- _posts/2017-06-04-Code-Structure-Principles.md
---



{% include load_video.html %}



Data lineage tracking is one of the significant problems that companies in highly regulated industries face.
These companies are required to have a good understanding of how data flows through their systems to comply with strict regulatory frameworks.
Many of these organizations also utilize big and fast data technologies such as Hadoop, Apache Spark and Kafka. Spark has become one of the most popular engines for big data computing.
In recent releases, Spark also provides the Structured Streaming component, which allows for real-time analysis and processing of streamed data from many sources.
[Spline](https://github.com/AbsaOSS/spline) is a data lineage tracking and visualization tool for Apache Spark.
Spline captures and stores lineage information from internal Spark execution plans in a lightweight, unobtrusive and easy to use manner.

Additionally, Spline offers a modern user interface that allows non-technical users to understand the logic of Apache Spark applications. In this presentation we cover the support of Spline for Structured Streaming and we demonstrate how data lineage can be captured for streaming applications.

Session hashtag: #SAISExp18

## Presentation:
[Spline presentation PDF download is here](/files/spline-data-lineage-for-spark-structured-streaming-saiseu2018.pdf) and [the conference page is here](https://databricks.com/session/spline-data-lineage-for-spark-structure-streaming).

<iframe src="//www.slideshare.net/slideshow/embed_code/key/31FGNIgkML7hdk" width="595" height="485" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/VaclavKosar/spline-data-lineage-for-spark-structure-streaming" title="Spline: Data Lineage For Spark Structured Streaming" target="_blank">Spline: Data Lineage For Spark Structured Streaming</a> </strong> from <strong><a href="//www.slideshare.net/VaclavKosar" target="_blank">Vaclav Kosar</a></strong> </div>

[//]: # ({% include load_slides.html %})

{% include image.html src="/images/2018-10-04-spark-summit-2.JPG" alt="Vaclav Kosar and Marek Novotny at Spark Summit 2018" %}


## About Authors

### About Vaclav Kosar
{% include image.html src="/images/vaclav-kosar-spark-ai-summit.png" alt="Vaclav Kosar" %}

Vaclav is a programming and analytics enthusiast. He currently forges big data software for ABSA R&D focusing on cruicial data lineage project Spline. He studied electronics, physics and mathematics.


### About Marek Novotny
Marek obtained bachelor and master degree in computer science at Charles University in Prague. His master studies were mainly focused on development of distributed and dependable systems. In 2013, Marek joined ABSA Capital in Prague to develop a scalable data integration platform and a framework for calculating regulatory reports. During the work on those two projects, he gained experience with many NoSQL and distributed technologies (e.g. Kafka, Zookeper, Spark). Nowadays, he is a member of Big Data Engineering team and primarily focused on development of the Spline project.

{% include image.html src="/images/marek-novotny-spark-ai-summit.png" alt="Marek Novotny" %}

{% include lets-connect.html %}

## Presentation Text

Spline: Data Lineage for Spark Structured Streaming

Marek Novotny, ABSA
Vaclav Kosar, ABSA

SAISExp18


About Us

- ABSA is a Pan-African financial services provider
- With Apache Spark at the core of its data engineering
- We try to fill gaps in the Hadoop eco-system
- Contributions to Apache Spark
- Spark-related open-source projects (github.com/AbsaOSS)
- ABRiS - Avro SerDe for structured APIs (#SAISDev5)
- Cobrix - Cobol data source
- Atum
- Completeness and accuracy library
- Spline - Data lineage tracking and visualization tool (#EUent3)

- How data is calculated?
- What is the schema and format of streamed data?
- To make Spark BCBS
(Clarity) compliant
- To communicate with business people
- Online documentation of
- Job dependencies
- Spark SQL job details
- Attributes occurring in the logic


Lineage Tracking of Batch Jobs
- Dataset-oriented
- Job
Leverages execution plans
- Structured APIs only
- SQL
- Dataframes
Dataset A
Lineage A
Datasets
- UDFs and lambdas are considered as black boxes

Lineage Tracking of Streaming Jobs
- Structured Streaming only
- App
Source-oriented (topic)
- Evolves in time


Structured Streaming Support
- StreamingQueryManager Spark structured streaming job
- Information about start
- Can provide execution Spark libraries
- Information about progress Session

StreamingQueryManager
- MicroBatch

Transformations
Start
Execution Plans
Progress
Query

Spline Streaming Listener Lineage Model
Event details
Spline UI
Interval View
- Displays data flow in fixed interval Job W1


Demo

What is temperature per hour in Prague?
- Use Case Output 2018-09-24
- Select Interval View
- Select Interval
- Select Sink
- Find Highlighted Sink
- Review The Lineage
- Change The Interval
- Observe New Lineage
- Select A Job
- Drill Down
- Review Job Details
- Select An Operation
- See Operation Attributes


Interval View Limitations

- Edge case (delayed read, early write)
- Job W1 should be linked
- Job W2 should not be linked Interval View

Lineage

Beyond The Interval View
- Instead of timestamp use Progress Event
addresses of rows Source 2
SS has addresses (offsets ) on each source, but not on sinks Job
- Most sinks are also sources and thus could return offsets Sink



Offset-Based Linking

- Jobs are linked when progress offsets overlap
- Offset timestamp doesn’t matter Job W1


Conclusion
- Spline: data lineage tracking tool
- New support for Structured Streaming
- Demo POC: Interval View
- Proposed generalization: offset-based linking



Future Plans

- Release Interval View in Spline
- After changes to Spark:
- Offset based linking for micro-batch streaming
- Continuous streaming support
- Support for dataset checkpoints


Questions

- Now is a good time
- Or feel free to contact us
- Marek Novotny
- Vaclav Kosar



