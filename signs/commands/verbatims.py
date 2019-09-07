class Verbatims:

    def __init__(self, text):

        self.text = text
        self.counter = len(text)

    def verbatims(self, keyword, no_of_words=1):

        # the output
        out = []

        # process the doc word-by-word
        for i in range(self.counter):
            try:
                if self.text[i] == keyword:
                    words = self.text[i-no_of_words:i+1+no_of_words]
                    out.append(' '.join(words))
            except IndexError:
                pass

        return out
