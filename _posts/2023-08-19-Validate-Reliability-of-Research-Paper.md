---
title: Validate Reliability of a Research Paper
description: Save time on diligence using 5 questions on authority, bias, evidence, comparison, impact based on Doomberg's framework, TRAAP Test, CRAAP Test, and RADAR.
categories: ml
date: 2023-08-19
last_modified_at: 2023-09-02
image: /images/symbols-of-truth.png
layout: post
permalink: /:categories/:title
my_related_post_paths:
- _posts/2023-07-04-How-to-Create-a-Machine-Learning-Dataset.md
- _posts/2023-03-26-David-Deutschs-Principles-in-Life-and-Business.md
- _posts/2020-04-22-result-diversification-in-web-search-and-recommenders.md
- _posts/2020-01-15-Quizrecall--Learn-any-text-with-automatically-generated-quiz.md
- _posts/2020-07-05-Transfigure-Stress-Into-Energy.md
- _posts/2016-11-04-Drone-Hackathoning.md
- _posts/2021-02-07-submodularity-in-ranking-summarization-and-self-attention.md
---

![symbols-of-truth](/images/symbols-of-truth.png)


Research is a large extent a media endeavour,
and so there is a large incentive to reach out for the fame by surprise breakthrough or confirmation the most extraordinary dreams and biases.
Common problems are unfair or irrelevant comparisons, or misunderstanding of what is measured.
To avoid wasting time on unlikely or irrelevant results, consider diligence methods below to analyze claim's validity.


## The Main Contribution's Relevance and Importance
Primary questions for each research to ask is:
1. What is the main idea in one sentence? Usually there is just one main idea, that can be summarized into one sentence even if you are not an expert in the research area. Lack of central point is suspicious.
2. What impact this may have and why is this important and relevant?
3. What are the unknowns and open questions? What does not fit well?


## Expanded Doomberg's 5 Question Framework
This is a expansion (ideas collected widely) of the questions mentioned in a podcast with Doomberg.
The most interesting set of questions, I came across were Doomberg's 5 questions that this independently thinking industry research group shared on a podcast. There is also a paywalled article [Conducting Diligence](https://doomberg.substack.com/p/conducting-diligence). I don't have full access to the text as of now.

1. Author Credibility: What is the reputation and history of the researchers and the institutions they are affiliated with?
  - Follow the money (Who benefits?):  Who funded it? Are researches biased, e.g. do their livelihoods, views, or identities tied to any of the results? For example, some research is funded by a for profit company, which they introduces goal-oriented bias into the research. (Try investing in a company and then tell me what it does to your views.). Is this disgruntled employee powered by resentment (Axe to grind)?
  - Connections: Who the author is connected to and who helped them in the past?
  - Outsider: Outsiders may shed new light, but with less authority on the subject.
2. Publisher Credibility: Who published these results in their publication? What is history and reputation of this publisher?
  - Reviewers and Critics: Who peer-reviewed or is it a self-published pre-print? Was the peer reviewer familiar with the domain to judge the research?
  - Republishers: Who is republishing the research and what are their biases, intentions, and incentives? Is this published by people from multiple sides?
  - Audience bias: Is there an existing bias in the audience that may have be preventing wider publication? Why was this published or surfaced now? Is the current environment related to the results?
3. Scientific Process and Evidence: At what stage is this research in the scientific process of validation and publishing?
  - How often are similar results invalid and retracted?
  - Burden of Evidence: What is the specific evidence for the claims? Are the comparisons valid? Or are there hidden effects? Is this Randomized double blind placebo control (RDBPC) trial?
  - Transparent: Is the process published and reliable? Are the numbers published and do they show reasonable statistical distribution? If you wanted to hide something, where it would you hide it?
4. Scientific Context: What does existing research and the history of this field suggest about these findings?
  - The idea: Is there clear main finding or an attempt to create confusion by adding unnecessary instead?
  - Shoulders of giants: What previous research this paper cites and stands on? What the assumptions and were they proven?
  - Cross check: Is the explanation for the claims correct? How does it compare to similar related research? Are the existing trends and order of magnitude estimates matching the results?
5. Future Expectations and Impact:
  - How large is the impact of the finding? Extraordinary claims require extraordinary proof.
  - When and how will these results be reproduced (replicated)? What industries are interested in applying this?
  - What are the risks, unknowns, and hidden problems that may invalidate the results or the impact?


## Other Claim Evaluation Tests

There are various tests:
1. The CRAAP Test: This easy to remember acronym stands for Currency, Relevance, Authority, Accuracy, and Purpose, and it guides users to assess the quality and relevance of information sources.

2. SIFT Method: The SIFT (Stop, Investigate the source, Find better coverage, Trace claims) method, is a simple four-step process for evaluating information online.

3. TRAAP Test: Similar to the CRAAP test, the TRAAP (Timeliness, Relevance, Authority, Audience and Purpose) test is used to assess the reliability of a source and the information it provides.

4. RADAR Framework: This stands for Rationale, Authority, Date, Accuracy, and Relevance. It essentially helps users to assess the quality, reliability, and usefulness of a resource.

5. PICO Framework: Used in evidence based practice to formulate a searchable clinical question. It stands for Patient problem or Population, Intervention, Comparison, and Outcome.


## Common Problems in Machine Learning Research
In machine learning, these are common problems that may be present in nice sounding research papers, which however will prove to offer no useful insights on how to improve the production systems in the industry.

- Evaluating architecture, but based on models with different parameter count. Bigger models will tend to outperform smaller models.
- Outperforming on unknown or invalid benchmarks: Evaluating general architecture ability, but using obscure benchmark dataset with only irrelevant competing architectures. Recommendation systems often lack large scale datasets to compare results on.
- Production-irrelevant metrics: Commonly in recommendation systems mean squared error was used for comparison, where as metrics like recall, NDCG, and precision are more useful for production deployments.
- Seed tuning, hyperparameters tuning or training more: Comparing with previous results, but spending more on finding the right random neural network initialization. This will inflate the results creating invalid comparison. Training time is part of the cost calculation for deployment.
- Testing set leak: Evaluating generalization, but having evaluation set samples leaking into the training set. This is difficult problem with web-scale datasets, which may be hard to filter out testing set.
- Different preprocessing or training set: Preprocessing, or filtering and training set may have much bigger impact than any model.
- Not reproducible: Not providing code and not providing all details about the path towards the results.
- Not citing research: Potential bias not to cite research from competing companies to avoid advertising them. However ignoring previous research may also exist because of limited research resources.


{% comment %}

This blog post, "Validate Reliability of a Research Paper," provides a valuable framework to critically evaluate research papers. However, a few areas could be improved or are missing:

1. Definition of terms: The blog jumps straight into detailed advice without providing a layman-friendly introduction to key concepts like Doomberg's framework, TRAAP Test, CRAAP Test, and RADAR.

2. Source credibility: Although the blog provides advice on checking the credibility of authors and publishers, there's no information about the credibility of the blog post author, which may undermine the trustworthiness of the advice given.

3. More detail on other tests: The five tests mentioned at the end are only briefly introduced without much explanation or practical advice on how to use them. More information or examples would help make the post more informative and useful.

4. Use of jargon: There are several instances of technical terms and jargon that might confuse readers who are not familiar with the subject matter. For instance, the term "Randomized double blind placebo control (RDBPC) trial" is casually dropped in without explanation. The author should either give a brief explanation or replace these terms with simpler alternatives.

5. Practical example: The guide would greatly benefit from a practical application or case study of these tests. This provides the reader with a concrete understanding of how they can apply these tests.

6. The structure of the content could be improved: The subsections tend to merge into one another and don't feel cohesive. Using clear, well-differentiated headers could aid in readability.

7. Argumentation: The post could present more robust arguments for why and when these different tests should be employed.

8. Tone and style: The blog post maintains a rather formal tone throughout, when it could be more conversational and engaging to fit the blog format and draw readers in. Adding a personal touch or opinions could add to the overall experience.

9. Conclusion: The post ends abruptly without summarizing the main points or giving a conclusion. A well-rounded conclusion could reinforce all the key takeaways for the readers.

{% endcomment %}