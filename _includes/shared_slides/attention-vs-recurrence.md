### Self-Attention vs Recurrent Layer
- attention vs recurrence = graph vs sequence = [Transformer](/ml/transformers-self-attention-mechanism-simplified) vs [LSTM](https://www.bioinf.jku.at/publications/older/2604.pdf) 
- attention connects across entire sequence as fully connected graph
- example graph task: [dependency parse](https://aclanthology.org/P05-1013.pdf) is a syntactic graph over the word sequence
- RRNs keeps information from previous states in a state vector as a memory
- RRNs not parallelizable in time dimension as future steps depend on the past
- RRNs have difficulty accessing long time ago information 
- RNNs handle repetition better, can use CTC Loss e.g. for OCR
- [SRU++](/ml/SRU++-Speeds-Up-Transformer-with-Simple-Recurrent-Unit-RNN) uses both attention and recurrence

{% include image.html src="/images/dependency-parse-tree.png" alt="Dependency parse tree example from Spacy" %}
