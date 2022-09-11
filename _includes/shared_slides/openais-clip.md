## OpenAI's CLIP
- [CLIP: Connecting Text and Images (Jan 2021)](https://openai.com/blog/clip/): encodes image, and text to similar embeddings
- dataset was proprietary WebImageText (WIT is not Wikipedia-based Image Text Dataset (WIT)) 400M of various images with a caption text from the internet
- now [open-source image-text datasets like LAION-400M available](https://laion.ai/blog/laion-400-open-dataset/), [open source CLIP models](https://github.com/mlfoundations/open_clip) as well
- trained with contrastive learning, maximizing cosine similarity of corresponding image and text
- image representations contain both style and semantics
- zero-shot classification, but fails on abstract or systematic tasks like counting

![CLIP contrastive pretraining](/images/clip-contrastive-pretraining.png)


### CLIP Architecture
- text and image have separate [transformer](/ml/transformers-self-attention-mechanism-simplified) encoders
- visual encoder is [ViT](https://arxiv.org/pdf/2010.11929.pdf) (vision [transformer](/ml/transformers-self-attention-mechanism-simplified))
- text encoder is [GPT-2](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) [transformer](/ml/transformers-self-attention-mechanism-simplified)
- the fixed-length text embedding is extracted from \[EOS\] token position,
- text token embeddings and image patch embeddings also available
- trained on 256 GPUs for 2 weeks

![CLIP architecture](/images/clip-architecture.png)


### CLIP Applications
- [DALL-E 1](/ml/openai-dall-e-2-and-dall-e-1#openais-dall-e-1) uses
  - [discrete variational autoencoder (dVAE)](/ml/openai-dall-e-2-and-dall-e-1#discreet-variational-auto-encoder-dvae), next token prediction,
  - and CLIP model for re-ranking,
- [DALL-E 2](/ml/openai-dall-e-2-and-dall-e-1#openais-dall-e-2)
  - uses CLIP embedding directly,
  - and decodes images via diffusion similar to [GLIDE](/ml/openai-dall-e-2-and-dall-e-1#openais-glide).
- zero-shot image classification:
  - create for each class a text -> embedding
  - cosine similarity between image and text embeddings
- [image-text classification](/ml/Multimodal-Image-Text-Classification)
  - sum up the two output class token embeddings zero-shot similar 
  - or the two output class token embeddings fed in to a shallow MLP classification head
  - or the two output sequences fed into a transformer with classification head
