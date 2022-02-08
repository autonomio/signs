from transformers import AutoModel, AutoTokenizer


class HuggingfaceEmbeddings:
    """
    Arguments:
        Checkpoint:
            Checkpoint name from huggingface model hub
    loads a `model` and `tokenizer` from huggingface from the given
        checkpoint if in local storage or huggingface hub
    """

    def __init__(self, checkpoint="prajjwal1/bert-small"):
        self.checkpoint = checkpoint
        self.tokenizer = AutoTokenizer.from_pretrained(self.checkpoint)
        self.model = AutoModel.from_pretrained(self.checkpoint)

    def generate_huggingface_embeddings(self, docs):
        """

        Arguments: `string` or a `list` of `strings` to be encoded.
        Generate huggingface embeddings.
        returns:
            tuple of tensors

        """
        model = self.model
        tokenizer = self.tokenizer
        inputs = tokenizer(docs, padding=True,
                           truncation=True, return_tensors="pt")
        outputs = model(**inputs)
        return outputs.last_hidden_state
