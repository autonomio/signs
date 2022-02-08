from transformers import AutoModel, AutoTokenizer


class HuggingfaceEmbeddings:
    """
    loads a `model` and `tokenizer` from huggingface from the given
        checkpoint if in local storage or huggingface hub
    Arguments:
        Checkpoint|str|Checkpoint name from huggingface model hub
    """

    def __init__(self, checkpoint="prajjwal1/bert-small"):
        self.checkpoint = checkpoint
        self.tokenizer = AutoTokenizer.from_pretrained(self.checkpoint)
        self.model = AutoModel.from_pretrained(self.checkpoint)

    def generate_huggingface_embeddings(self, docs):
        """
        Generate huggingface embeddings.
        Arguments:
            docs|`string` or a `list` of `strings`
        returns:
            tuple of tensors

        """
        model = self.model
        tokenizer = self.tokenizer
        inputs = tokenizer(docs, padding=True,
                           truncation=True, return_tensors="pt")
        outputs = model(**inputs)
        return outputs.last_hidden_state
