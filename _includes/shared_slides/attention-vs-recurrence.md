### Attention vs Recurrence
- attention vs recurrence = graph vs sequence
- attention connects across entire sequence as fully connected graph
  - [dependency parse](https://aclanthology.org/P05-1013.pdf) is a syntactic graph over the word sequence
- recurrence keeps information from previous states in a state vector
- [original recurrent LSTM](https://www.bioinf.jku.at/publications/older/2604.pdf) is less parallelizable than [Transformer](https://arxiv.org/pdf/1706.03762v5.pdf)
  - future steps in LSTM depend on the past and is not parallelizable

![Dependency parsing and sequence from Standford Speech and Language Processing Daniel Jurafsky & James H. Martin](/images/dependency-parse-tree.png)
