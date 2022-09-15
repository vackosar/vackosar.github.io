## The Simplest Document Representations
- Once were paper archives replaced with databases of textual documents some tasks became cheaper: search by list of words (query) ~1970s, finding document topics ~1980
- simplest methods: counting word occurrences on documents level into [sparce matrices](/ml/sparse-matrix-why-and-when) as feature vectors in methods term frequency–inverse document frequency (TF-IDF), [Latent semantic analysis (LSA)](https://www.cs.bham.ac.uk/~pxt/IDA/lsa_ind.pdf)
- this co-occurrence of words in documents later used to embed words

![Latent semantic analysis (LSA) - CC BY-SA 4.0 Christoph Carl Kling](/images/latent-semantic-analysis-wiki.png)


## Non-Contextual Words Vectors
- document split into sentence sized running window of 10 words
- each of 10k sparsely coded vocabulary words is mapped (embedded) to a vector into a 300 dimensional space
- the embeddings are [compressed](/ml/neural-data-compression) as only 300 dimensions much less than 10k vocabulary feature vectors
- the embeddings are dense as the vector norm is not allowed to grow too large
- these word vectors are non-contextual (global), so we cannot disambiguate fruit (flowering) from fruit (food)

![word2vec](/images/word2vec-10k-tensorflow-projector.png)


## Word2vec Method for Non-contextual Word Vectors
- [word2vec (Mikolov 2013)](https://arxiv.org/pdf/1301.3781.pdf): 10 surrounding words embeddings trained to sum up close to the middle word vector
- even simpler method: [GloVe (Pennington 2014)](https://nlp.stanford.edu/pubs/glove.pdf): just counting co-occurrence in a 10 word window 
- other similar methods: [FastText](/ml/FastText-Vector-Norms-And-OOV-Words), [StarSpace](/ml/starspace-embedding) 
- words appearing in similar context have similar embedding vectors 
- word disambiguation is not supported

![word2vec operation](/images/word2vec.jpg)


## Knowledge Graph's Nodes Are Disambiguated
- knowledge graph (KG) e.g. Wikidata: each node is specific fruit (flowering) vs fruit (food)
- KG is an imperfect tradeoff between database and training data samples
- Wikipedia and the internet are something between knowledge graph and set of documents
- random walks over KG are valid "sentences", which can be used to train node embeddings e.g. with Word2vec (see "link prediction")

![knowledge graph visualization from wikipedia](/images/knowledge-graph.jpg)


## Contextual Word Vectors
- imagine there is a node for each specific meaning of each word in hypothetical knowledge graph
- given a word in a text of 100s of words, the specific surrounding words locate our position within the knowledge graph, and identify the word's meaning
- two popular model architectures incorporate context:
  - [recurrent neural networks (LSTM, GRU)](/ml/SRU++-Speeds-Up-Transformer-with-Simple-Recurrent-Unit-RNN) are sequential models with memory units
  - [transformer architecture](/ml/transformers-self-attention-mechanism-simplified) consumes the entire input sequence is State-of-the-art 2022

![transformer from word2vec](/images/transformer-from-word2vec.jpg)
