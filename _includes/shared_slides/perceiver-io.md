
[Perceiver IO](https://arxiv.org/pdf/2107.14795.pdf) is a general-purpose multi-modal architecture that can handle wide variety of inputs as well as outputs.
Perceiver can be applied to for example [image-text classification](/ml/Multimodal-Image-Text-Classification).
Perceiver IO uses [cross-attention](/ml/cross-attention-in-transformer-architecture) for merging:
- multimodal input sequences (e.g. image, text, audio) into a low dimensional latent sequence
- "output query" or "command" to decode the output value e.g. predict this masked word

{% include image.html src="/images/cross-attention-perceiver-io.png" alt="Perceiver IO architecture" %}

Advantage of the Perceiver architecture is that in general you can work with very large inputs.
Architecture [Hierarchical Perceiver](https://arxiv.org/pdf/2202.10890.pdf) has ability to process even longer input sequences by splitting into subsequences and then merging them.
Hierarchical Perceiver also learns the positional encodings with a separate training step with a reconstruction loss.
