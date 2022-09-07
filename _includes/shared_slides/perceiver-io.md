
[Perceiver IO](https://arxiv.org/pdf/2107.14795.pdf) is a general-purpose multi-modal architecture that can handle variety of inputs and outputs.
Perceiver IO uses [cross-attention](/ml/cross-attention-in-transformer-architecture) for:
- merging very long input sequences (e.g. images, audio) into the low dimensional latent embeddings sequence
- merging "output query" or "command" to decode the output value e.g. we can the model ask about a masked word

![Perceiver IO architecture](/images/cross-attention-perceiver-io.png)


Advantage of this is that in general you can work with very long sequences.
Architecture [Hierarchical Perceiver](https://arxiv.org/pdf/2202.10890.pdf) has ability to process even longer sequences by splitting into subsequences and then merging them.
Hierarchical Perceiver also learns the positional encodings with a separate training step with a reconstruction loss.
