In 2023, [sparse representations](/ml/sparse-matrix-why-and-when) also appeared in practise in the **Sparse Mixture-of-Experts** deep-learning architecture exemplified by widely-used Mixtral model. In each [feed-forward layer](/ml/Feed-Forward-Self-Attendion-Key-Value-Memory) of Mixtral model, only 2 of 8 (25%) get activated during inference.    

<blockquote class="blockquote" style="font-style: italic">
Mixtral is a sparse mixture-of-experts network. It is a decoder-only model where the feedforward block picks from a set of 8 distinct groups of parameters. At every layer, for every token, a router network chooses two of these groups (the “experts”) to process the token and combine their output additively.
<footer class="blockquote-footer"><a href="https://mistral.ai/news/mixtral-of-experts/">Mistral.ai</a></footer>
</blockquote>
