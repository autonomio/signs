from .commands.embeds import Embeds
from .commands.clean import Clean
from .commands.preds import Preds
from .commands.load_vectors import LoadVectors
from .commands.verbatims import Verbatims
from .grams.grams import Grams
from .vectorize.gensim_doc2vec_train import gensim_doc2vec_train as TrainDoc2Vec
import signs.preprocess

__all__ = ['Embeds', 'Clean', 'Preds', 'LoadVectors', 'Grams']

del commands, utils, grams, vectorize, signs
