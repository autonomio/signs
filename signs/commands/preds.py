import pandas as pd
from ..utils.converters import embeds_to_text
try:
    from kerasplotlib.text import text
except ImportError:
    print('Matplotlib failed to import')


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

    def _printing(self, data, title, n, notebook):

        data.drop_duplicates(inplace=True)

        if notebook:
            text(data, 'text', title=title)
        else:
            print(title)
            for t in data['text'].head(n):
                print(t)
            print('\n')


    def summary(self, sensitivity=.1, n=5, notebook=True):

        '''Provides a summary of the classification results for the model

        sensitivity : float
             Cut-off point for deciding between positive and negative.
        n : int
             Number of samples to display.
        notebook : bool
             Use html printing for notebooks.

        '''

        pos = self.results[self.results.pred > 1 - sensitivity].sample(n, replace=True)
        self._printing(pos, 'CLEAR POSITIVE', n, notebook)

        mid = self.results[self.results.pred.between(0.5 - (sensitivity / 2), 0.5 + (sensitivity / 2))].sample(n, replace=True)
        self._printing(mid, 'CLOSE CALL', n, notebook)

        neg = self.results[self.results.pred < sensitivity].sample(n, replace=True)
        self._printing(neg, 'CLEAR NEGATIVE', n, notebook)


    def misses(self, sensitivity=.5, n=5, notebook=True):

        '''Random examples of false positives and false negatives

        sensitivity : float
             Cut-off point for deciding between positive and negative.
        n : int
             Number of samples to display.
        notebook : bool
             Use html printing for notebooks.

        '''

        # false positive
        fp = self.results[self.results.truth == 0][self.results.pred > 1 - sensitivity].sample(n, replace=True)
        self._printing(fp, 'FALSE POSITIVE', n, notebook)

        # false negatives
        fn = self.results[self.results.truth == 1][self.results.pred < sensitivity].sample(n, replace=True)
        self._printing(fn, 'FALSE NEGATIVE', n, notebook)

    def hits(self, sensitivity=.1, n=5, notebook=True):

        '''Random examples of true positives and true negatives

        sensitivity : float
             Cut-off point for deciding between positive and negative.
        n : int
             Number of samples to display.
        notebook : bool
             Use html printing for notebooks.

        '''

        # true positive
        tp = self.results[self.results.truth == 1][self.results.pred > 1 - sensitivity].sample(n, replace=True)
        self._printing(tp, 'TRUE POSITIVE', n, notebook)

        # true negatives
        tn = self.results[self.results.truth == 0][self.results.pred < sensitivity].sample(n, replace=True)
        self._printing(tn, 'TRUE NEGATIVE', n, notebook)
