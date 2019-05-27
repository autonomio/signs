from .commands.embeds import Embeds
from .commands.clean import Clean
from .commands.preds import Preds
from .commands.load_vectors import LoadVectors
from .commands.verbatims import Verbatims
from .commands.describe import Describe
from .commands.transform import Transform
from .commands.docsimilarity import DocSimilarity
from .commands.stopwords import Stopwords
from .commands.autoprep import AutoPrep

from .grams.grams import Grams
from .vectorize.gensim_doc2vec_train import gensim_doc2vec_train as TrainDoc2Vec
import signs.preprocess

__all__ = ['Embeds', 'Clean', 'Preds', 'LoadVectors', 'Grams', 'Describe', 'Transform']

del commands, utils, grams, vectorize, signs
