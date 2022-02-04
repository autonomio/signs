from sentence_transformers import SentenceTransformer

class SentenceEmbeddings:
    """
    Loads model available from from sbert.net
    """
    def __init__(self,checkpoint="paraphrase-MiniLM-L6-v2"):
        self.checkpoint=checkpoint
        self.model=SentenceTransformer(checkpoint)
    def generate_sentence_embeddings(self,docs):
        """
        Generates sentence embeddings
        Arguments: 
            `Docs`: `String` or `List` of `Strings`
        
        """
        return self.model.encode(docs)