 
- [Tokenization](/ml/Tokenization-in-Machine-Learning-Explained) is cutting input data into parts ([symbols](/ml/Symbolic-vs-Connectionist-Machine-Learning)) that can be [mapped (embedded)](/ml/Embeddings-in-Machine-Learning-Explained) into a vector space.
- For example, input text is split into frequent words e.g. [transformer tokenization](/ml/transformer-embeddings-and-tokenization).
- Sometimes we append special tokens to the sequence e.g. class token (\[CLS\]) used for classification embedding in [BERT transformer](/ml/transformers-self-attention-mechanism-simplified).
- Tokens are mapped to vectors ([embedded, represented](/ml/Embeddings-in-Machine-Learning-Explained)), which are passed into neural neural networks.
- [Token sequence position itself is often vectorized and added to the word embeddings (positional encodings)](/ml/transformer-positional-embeddings-and-encodings).