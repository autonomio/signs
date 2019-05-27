class Stopwords:

    def __init__(self,
                 docs,
                 common_stopwords=True,
                 add_stopwords=[],
                 min_length=2,
                 max_threshold=10):

        '''Accepts as input a list-of-lists where
        each sublist is a document represented in tokens.

        docs : list (of lists)
            Tokenized documents.
        common_stopwords : bool
            If a comprehensive list of stopwords should be used. If set
            to False then add_stopwords can't be empty.
        add_stopwords : list or None
            If a list of words is provided, then those will be used
            as well as common_stopwords unless it's set to False.
        min_lenght : int
            Drop all words below this length.
        max_threshold : int
            Keep all words that are at least this long.

        '''

        import string

        self.common_stopwords = common_stopwords
        self.add_stopwords = add_stopwords
        self.min_length = min_length
        self.max_threshold = max_threshold

        self.string = string
        self.stopwords = self.stopword_index()
        self.docs = docs

        for i in range(len(docs)):
            self.docs[i] = self.check_stopwords(docs[i])

    def stopword_index(self):

        import numpy as np

        out = []

        if self.common_stopwords is True:
            from signs.utils.stopwords import stopwords
            stopword_list = np.unique(stopwords()).tolist()
            stopword_list + self.add_stopwords
        else:
            stopword_list = self.add_stopwords

        for word in stopword_list:
            if len(word) > 1:
                out.append(word.lower())

        stopword_dict = {}

        for word in out:

            if word[0] in self.string.ascii_letters:
                try:
                    stopword_dict[word[0]].append(word)
                except KeyError:
                    stopword_dict[word[0]] = [word]

        return stopword_dict

    def check_stopwords(self, doc):

        out = []

        for word in doc:

            # always keep words longer than 10 characters
            if len(word) >= self.max_threshold:
                out.append(word)

            # always pass words shorter than 2 characters
            elif len(word) <= self.min_length:
                continue

            elif word[0] not in self.stopwords.keys():
                out.append(word)

            elif word not in self.stopwords[word[0]]:
                out.append(word)

        return out
