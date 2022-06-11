## Rotary Position Embedding (RoPE)
- introduced in [RoPE Embeddings in RoFormer](https://arxiv.org/pdf/2104.09864.pdf)
- want relative position info in query-value dot-product
- use multiplicative rotational matrix mixing pairwise neighboring dimensions
- improves accuracy on long sequences?
- poor results also reported: [tweet 1](https://twitter.com/BlancheMinerva/status/1394089508723900422?s=20&t=25ryLN42GEzy_m4xaqagBw), [tweet 2](https://twitter.com/OfirPress/status/1477641091071590400)
- used in Google's [$10M model PaLM](/ml/googles-pathways-language-model-and-chain-of-thought)
