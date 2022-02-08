from sentence_transformers import SentenceTransformer


class SentenceEmbeddings:
    """
    Arguments:
        Checkpoint: model name avaialable from sbert.net
    Loads model available from from sbert.net
    """

    def __init__(self, checkpoint="paraphrase-MiniLM-L6-v2"):
        self.checkpoint = checkpoint
        self.model = SentenceTransformer(checkpoint)

    def generate_sentence_embeddings(self, docs):
        """
        Arguments:
            `Docs`: `String` or `List` of `Strings`
        Generates sentence embeddings
        Returns:
            list of embeddings

        """
        return self.model.encode(docs)
