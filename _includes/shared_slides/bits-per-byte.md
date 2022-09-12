
- compression ratio is defined as \\( \mathrm{cmpRatio} = \mathrm{unCompressedBytes} / \mathrm{compressedBytes} \\)
- Bits-per-byte is defined as \\(  \mathrm{compressedBits} / \mathrm{unCompressedBytes} \\)
- Bits-per-byte (bpb) metric is inverse compression ratio divided by 8: \\( 1 bpb = 1 / (8 \mathrm{cmpRatio}) \\).
- Bits-per-character (bpc) metric for ASCII Extended characters equals bits-per-byte (bpb).
- Cross-entropy loss using log2 for a character-level language model averaged over a dataset equals bpc.
- Gzip compresses enwik8 2.92 bpb, Morse code approximately 10.8 bpc
- [SRU++](/ml/SRU++-Speeds-Up-Transformer-with-Simple-Recurrent-Unit-RNN) model achieves 1.02 bpc - approximately compression ratio of 8
 