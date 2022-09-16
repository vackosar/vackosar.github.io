 
- [Tokenization](/ml/Tokenization-in-Machine-Learning-Explained) is cutting input data into meaningful parts that can be [embedded](/ml/Embeddings-in-Machine-Learning-Explained) into a vector space.
- image is split into patches, text is split into tokens (words) e.g. [transformer tokenization](/ml/transformer-embeddings-and-tokenization)
- Sometimes we also add [token position is added to their embeddings](/ml/transformer-positional-embeddings-and-encodings).

### Tokenization in NLP
- Input data text is split using a dictionary into character chunks called tokens
- The vocabulary contains around 100k most common sequences from the training text.
- Tokens often correspond to words of 4 characters long with prepended whitespace or special characters.
- common tokenization algorithms are [BPE](/ml/Tokenization-in-Machine-Learning-Explained#bpe-tokenizer), [WordPiece](/ml/Tokenization-in-Machine-Learning-Explained#wordpiece-vs-bpe-tokenizer), [SentencePiece](/ml/Tokenization-in-Machine-Learning-Explained#sentencepiece-vs-wordpiece-tokenizer)
- Text tokens can be converted back to text, but sometimes there is a loss of information.

![tokenization and embedding layer for transformer](/images/transformer-tokenization-and-embeddings.drawio.svg)


### Tokenization In Continuous Modalities Vision or Speech
- Tokenizers are not quite present in modalities like image or speech.
- Instead, the images or audio is split into a matrix of patches without dictionary equivalent as in case of the text.
- Image architectures [Vision Transformer (ViT)](https://arxiv.org/pdf/1909.02950.pdf), Resnets split image into overlapping patches and then encode these.
- Outputs [embeddings](/ml/Embeddings-in-Machine-Learning-Explained) of these can then be passed to a transformer e.g. in [CMA-CLIP or MMBT](/ml/Multimodal-Image-Text-Classification#amazons-cma-clip-model)

![tokenization and embedding in Vision Transformer ViT](/images/vision-transformer-vit-architecture.png)


#### Quantization

{% include  shared_slides/quantization.md %}
