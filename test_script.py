from tests.test_clean import test_clean
from tests.test_stopwords import test_stopwords
from tests import utils_file
from tests import vectorize_spacy
# from signs.tests import vectorize_gensim

print('Testing Clean() ... \n')
test_clean()

print('Testing Stopwords() ... \n')
test_stopwords()

utils_file.run_test()
vectorize_spacy.run_test()
# vectorize_gensim.run_test()
