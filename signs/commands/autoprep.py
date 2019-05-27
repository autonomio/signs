class AutoPrep:

    def __init__(self, docs):

        self.docs = self._format(docs)
        self.docs = self._clean()

    def _format(self, docs):

        # input is a single string
        if isinstance(docs, str):
            pass
        # input is list with strings
        if isinstance(docs[0], str):
            pass
        # input is list with lists
        if isinstance(docs[0], list):
            pass

    def _clean(self):

        from signs import Clean
        return [[Clean(doc).text] for doc in self.docs]
