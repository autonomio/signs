from tests.test_clean import test_clean
from tests.test_grams import test_grams
from tests.test_stopwords import test_stopwords
from tests.test_vectorize_spacy import test_vectorize_spacy
from tests.test_read_file import test_read_file
from tests.test_transform import test_transform

print('Testing Clean() ...')
test_clean()

print('Testing Grams() ...')
test_grams()

print('Testing Stopwords() ...')
test_stopwords()

print('Testing Transform() ...')
test_transform()

print('Testing vectorize_spacy()')
test_vectorize_spacy()

print('Testing read_file()')
test_read_file()
