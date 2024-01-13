---
title: Validate Reliability of a Research Paper
description: Save time on diligence using 5 questions on authority, bias, evidence, comparison, impact based on Doomberg's framework, common Ray Dalio's believability, TRAAP Test, CRAAP Test, RADAR.
categories: ml
date: 2023-08-19
last_modified_at: 2023-09-02
image: /images/symbols-of-truth.png
video: O9fxWCaDM4o
layout: post
permalink: /:categories/:title
my_related_post_paths:
- _posts/2023-03-26-David-Deutschs-Principles-in-Life-and-Business.md
- _posts/2020-04-22-result-diversification-in-web-search-and-recommenders.md
- _posts/2023-07-04-How-to-Create-a-Machine-Learning-Dataset.md
- _posts/2022-01-09-7-powers-moats-through-lens-of-dibellos-business-mental-model.md
- _posts/2021-12-12-Ten-Commandments-for-business-failure.md
- _posts/2020-07-05-Transfigure-Stress-Into-Energy.md
- _posts/2022-04-13-openai-dall-e-2-and-dall-e-1.md
---


{% include load_video.html %}


Research is, to a large extent, a media endeavor,
and so there is a significant incentive to reach out for fame with a surprise breakthrough or confirmation of the most extraordinary dreams and biases.
However, common problems, such as unfair or irrelevant comparisons or misunderstandings regarding what is measured, riddle the writings.
To avoid wasting time on unlikely or irrelevant results, consider using the diligence methods below to analyze a claim's credibility or believability (correctness, completeness, and importance), because even valid results may take you nowhere in your business territory.


## The Main Contribution Relevance, Impact, and Open Questions
The primary questions to ask when looking at a piece of research to ask are:
1. What is the main idea in one sentence? Usually, there is just one main idea that can be summarized into one sentence, even if you are not an expert in the research area. The lack of a central point is suspicious.
2. What impact could this have, and why is this important and relevant?
3. What are the unknowns and open questions? What does not fit well?


## Expanding on Doomberg's 5 Question Framework
The most exciting questions I encountered were Doomberg's 5 questions shared on [a podcast](https://www.youtube.com/watch?v=2hCu2eRRGUI).
Doomberg is an independently thinking industry research group.
This post is an expansion of the 5 questions.
There is a paywalled article called [Conducting Diligence](https://doomberg.substack.com/p/conducting-diligence) with all the details, but I don't have full access to the text as of now.

1. Author Credibility: What is the reputation and history of the researchers and the institutions they are affiliated with? Do they have at least 3 successes within the domain?
  - Follow the money (Who benefits?): Who funded it? Are researchers biased, e.g., are their livelihoods, views, or identities tied to any results? For example, some research is funded by a for-profit company, which they a goal-oriented bias into the study. (Try investing in a company and then tell me what it does to your views.). Is this a disgruntled employee powered by resentment (Axe to grind)?
  - Connections: Are they known, accessible, or anonymous? Who is the author connected to, and who helped them in the past?
  - Outsider: Outsiders may shed new light with less authority on the subject.
2. Publisher Credibility: Who published these results in their publication? What is the history and reputation of this publisher?
  - Reviewers and Critics: Who peer-reviewed, or is it a self-published pre-print? Was the peer reviewer familiar with the domain to judge the research?
  - Republishers: Who are the original primary sources, and are they publicly accessible and non-anonymous? Who is republishing the research, and what are their biases, intentions, and incentives? Do people from multiple sides publish this?
  - Audience bias: Is there an existing bias in the audience that may have been preventing wider publication? Why was this published or surfaced now? Is the current environment related to the results?
3. Scientific Process and Evidence: At what stage is this research in the scientific process of validation and publishing?
  - How often are similar papers at similar stage invalid and retracted?
  - Burden of Evidence: What is the specific evidence for the claims and does it really imply the conclusion (non sequitur)? Are the metrics and their comparisons valid and relevant? Or are there hidden effects? Is this a randomized double-blind placebo control (RDBPC) trial?
  - Transparent: Is the process published and reliable? Are the numbers published, and do they show reasonable statistical distribution? If you wanted to hide something, where would you hide it?
4. Scientific Context: What do existing research and the history of this field suggest about these findings?
  - The idea: Is there a clear main finding or an attempt to create confusion by adding unnecessary instead? Is the main message coherent? Does the title match the content?
  - Shoulders of Giants: What previous research does this paper cite and stand on? Are the cited sources saying what is claimed this paper? What are the assumptions, and were they proven?
  - Cross-check: Is the explanation for the claims correct? How does it compare to similar related research? Do the existing trends and order of magnitude estimates match the results?
5. Future Expectations and Impact: What is the outlook for this finding
  - How large is the impact of the finding? Extraordinary claims require extraordinary proof. How large are the rewards for the successful implementation of this method?
  - When and how will these results be reproduced (replicated)? What industries are interested in applying this? Who wants to put this into production?
  - What are the risks, unknowns, and hidden problems that may invalidate the results or the impact, and how likely they are? What is the downside if you experiment with this method?


## Common Problems in Machine Learning Research
In machine learning, these are common problems that may be present in nice-sounding research papers, which, however, will prove to offer no valuable insights on how to improve the production systems in the industry.

- Evaluating architecture, but based on models with different parameter counts. Bigger models will tend to outperform smaller models.
- Outperforming on unknown or invalid benchmarks: Evaluating general architecture ability but using obscure benchmark datasets with only irrelevant competing architectures. Recommendation systems often lack large-scale datasets to compare results on.
- Production-irrelevant metrics: Commonly, in recommendation systems mean squared error was used for comparison, whereas metrics like recall, NDCG, and precision are more useful for production deployments.
- Seed tuning, hyperparameter tuning, or training longer: Comparing with previous results, but spending more on finding the best random neural network initialization. This will inflate the results, creating invalid comparisons. Training time is part of the cost calculation for deployment.
- Testing set leak: Evaluating generalization but having evaluation set samples leaking into the training set. This is a difficult problem with web-scale datasets, which makes it hard to filter out testing sets.
- Different preprocessing or training sets: Preprocessing and filtering of the training set may have a much more significant impact than any model.
- Not reproducible: Not providing code and not providing all details about the path towards the results.
- Not citing research: Potential bias not to cite research from competing companies to avoid advertising them. However, ignoring previous research may also exist because of limited research resources.
- Authors that had large impact on ML in the past (incomplete): Schmidhuber, Hinton, Karpathy, Bengio, Lecun 

## Other Claim Evaluation Tests

There are various tests:

1. Ray Dalio's Believability: "People who have repeatedly and successfully accomplished the thing in question and have great explanations when probed are most believable."

2. The CRAAP Test: This easy-to-remember acronym stands for Currency, Relevance, Authority, Accuracy, and Purpose, and it guides users to assess the quality and relevance of information sources.

3. SIFT Method: The SIFT (Stop, Investigate the source, Find better coverage, Trace claims) method is a simple four-step process for evaluating information online.

4. TRAAP Test: Similar to the CRAAP test, the TRAAP (Timeliness, Relevance, Authority, Audience, and Purpose) test is used to assess the reliability of a source and the information it provides.

5. RADAR Framework: This stands for Rationale, Authority, Date, Accuracy, and Relevance. It essentially helps users to assess the quality, reliability, and usefulness of a resource.

6. PICO Framework: Used in evidence-based practice to formulate a searchable clinical question. It stands for Patient problem or Population, Intervention, Comparison, and Outcome.


## Battle Testing the Method
It is great to have a handy set of questions to ask to assess credibility quickly.
But you will only know the usefulness once you apply the method correctly and completely yourself in your particular problem terrain.
Depending on your business territory, this may or may not be worth your time.



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