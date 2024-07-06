---
title: Precision and Recall Intuitive Mnemonic
description: Remember the precision and recall definitions with this visual story.
categories: ml
date: 2024-07-06
last_modified_at: 2024-07-06
layout: post
permalink: /:categories/:title
---

{% include highlight-rouge-friendly.css.html %}


Precision and recall are fundamental metrics used in machine learning classification. However, it may be hard to remember the definitions. Below is a mnemonic that could help you remember or learn precision and recall better.

You pick good apples and put them into your _basket_, while throwing the bad ones into the trash bucket. However, you have a hard time quickly recognizing the good apples from the bad ones quickly. So, you often have to guess. Once you are done, you would like to measure how well you guessed.

There are many ways to measure, but people often use precision and recall metrics for classification problems like this.


## Precision Mnemonic

Am I _precise_ and selected truly _good apples_ into _the basket_?
Precisely, I don't select any bad apple into the basket!
Good apples is precisely what I selected?
Of all the apples I picked (selected), how many are actually good?

The basket of selected (relevant, `n_selected`) apples are the positive predictions.

`n_selected = n_true_positives + n_false_positives`

So precision is:
```
precision = true_positives / n_selected
precision = true_positives / (true_positives + n_false_positives)
```

Precision is related to quality.



## Recall Mnemonic

Did I have sensitive _recall_ and _selected all the good apples_ from _the good apples_?
Recall, I don't forget any good apple from the tree!
I selected all the good apples with total recall?
Of all the good apples available, how many did I actually pick?

The good apples are the positive (`n_positives`) samples.

`n_positives = n_true_positives + n_false_negatives`

So recall is:
```
recall = true_positives / n_positives
recall = true_positives / (true_positives + n_false_negatives)
```

Recall is the same as sensitivity and is related to completeness, quantity.