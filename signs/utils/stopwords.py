# coding=utf-8

from nltk.corpus import stopwords as nltk_stopwords
import string


def stopwords():

    # STOPWORDS MODULE

    # Here we are creating various lists of words
    # in to one list 'check' which is then later
    # iterated against

    nltk_stop = nltk_stopwords.words('english')
    punctuation_stop = list(string.punctuation)
    numeric_stop = list(range(30))
    twitter_stop = ['RT', 'http', 'https', 'rt', 'via']
    generic_stop = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','1','2','3','4','5','6','7','8','9','0',
                     'was','are','going','used','&amp;','has','dont','amp',
                     'the','be','and','of','a','in','to','is','i','an',
                     'have','to','it','I','that','for','you','why','were',
                     'he','with','on','do','say','this','they','had','been',
                     'at','but','we','his','from','that','not','\"the',
                     'by','she','or','as','what','go','their','did',
                     'can','who','get','if','would','her','all','you.',
                     'my','make','about','know','will','as','up','let',
                     'one','time','there','so','when','which','them','did',
                     'some','me','take','out','into','just','see','him',
                     'your','come','could','now','than','like','other',
                     'how','then','its','our','two','more','these','don\'t',
                     'want','way','look','first','also','new','because',
                     'day','more','use','no','man','find','here','thing',
                     'give','many','well','only','those','tell','one',
                     'very','her','even','back','any','good','through',
                     'us','there','down','may','should','over','still',
                     'try','in','as','last','ask','need','too','feel',
                     'three','when','never','become','between','high','each',
                     'really','something','most','another','much','own','both',
                     'out','leave','put','old','while','mean','it\'s','week.'
                     'clinton\'s','im','u','i\'m','said','de','http','https','got',
                     'didn\'t','doesnt','didnt\…','i\'d','can\'t','doesn\'t',
                     'isn\'t','\“what\’s','ever','again.','()','thought',
                     'before','after','2016','knows','everyone','every','please']

    check = nltk_stop + punctuation_stop + numeric_stop + twitter_stop + generic_stop

    return check