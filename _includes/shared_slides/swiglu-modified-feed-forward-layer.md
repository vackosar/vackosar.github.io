## SwiGLU Modified Feed-Forward Layer
- instead of RELU \\( max(0, xW_1 + b_1)W_2 + b_2 \\) uses [SwiGLU](https://arxiv.org/pdf/2002.05202.pdf) \\( (\mathrm{Swish}(xW_1) \otimes xV ) W_2 \\)
- gated linear unit (GLU) is a sigmoid controlled output
- midly similar to [cross-attention with a static sequence](/ml/Feed-Forward-Self-Attendion-Key-Value-Memory)
- ~1% higher accuracy in compute equivalent setup
- [swish activation](https://arxiv.org/pdf/1710.05941v1.pdf?source=post_page): \\( \mathrm{Swish}(x) := x (1 + exp(−x))^{−1} \\)
- used in [PaLM model](/ml/googles-pathways-language-model-and-chain-of-thought)
