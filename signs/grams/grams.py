class Grams:
    
    def __init__(self, text):

        '''Takes in a list of words representing a document
        and returns a list of ngrams or skipgrams.

        text : list
            A list of words representing a document.

        '''

        self.text = text
        self.counter = len(text)

    def ngrams(self, ngram=2, skip=0):

        '''Produce ngrams or skipgrams.

        ngram: int
            Number of words per gram.
        skip : int
            The number of words to skip for each gram'''
        
        # the output
        out = []

        # process the doc word-by-word
        for i in range(self.counter):
            try:
                # create the list for single instance of grams
                words = [self.text[i]]
                
                # find the grams
                for ii in range(ngram - 1):
                    words.append(self.text[i + ii + 1 + skip])
            
                # add to the output
                out.append(words)
            
            # handle the case where end is near
            except IndexError:
                pass

        return out