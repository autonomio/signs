import pandas as pd
from .converters import embeds_to_text
from kerasplotlib.text import text


class Preds:

    def __init__(self, x_test, y_test, word_index, model):

        # temp values
        self.model = model
        self.x_test = x_test
        self.y_test = y_test
        self.word_index = word_index

        self.results = self._preds_df()

        # delete temp values
        del self.word_index, self.y_test, self.x_test, self.model

    def _preds_df(self):

        '''
        x_test :: the test data (already embedded)
        y_test :: truth values for the test data
        word_index :: the word index used for creating the embeddings

        '''

        results = pd.DataFrame({
                    'text': embeds_to_text(self.x_test, self.word_index),
                    'pred': [i[0] for i in self.model.predict(self.x_test)],
                    'truth': self.y_test
                            })

        return results

    def summary(self, sensitivity=.1, n=5):

        pos = self.results[self.results.pred > 1 - sensitivity].sample(n, replace=True)
        text(pos, 'text', title='Clear Positive')

        mid = self.results[self.results.pred.between(0.5 - (sensitivity / 2), 0.5 + (sensitivity / 2))].sample(n, replace=True)
        text(mid, 'text', title='Close Call', max_rows=5)

        neg = self.results[self.results.pred < sensitivity].sample(n, replace=True)
        text(neg, 'text', title='Clear Negative', max_rows=5)

    def falses(self, sensitivity=.1, n=5):

        # false positive
        fp = self.results[self.results.truth == 0][self.results.pred > 1 - sensitivity].sample(n, replace=True)
        text(fp, 'text', title='False Positives')

        # false negatives
        fn = self.results[self.results.truth == 1][self.results.pred < sensitivity].sample(n, replace=True)
        text(fn, 'text', title='False Negatives')
