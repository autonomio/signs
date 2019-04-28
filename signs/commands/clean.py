import re
import string

from ..utils.stopwords import stopwords


class Clean:
    
    def __init__(self, text, auto=False, remove_string=''):

        self.remove_string = remove_string

        if isinstance(text, list):
            self.text = text[0]
        else:
            self.text = text

        if auto:
            if self.text is None:
                pass
            else:
                self.automated()

    def automated(self):

        self.text = self.decod()
        self.text = self.low()
        self.text = self.links()
        self.text = self.emoji()
        self.text = self.punct()
        self.text = self.linebreaks()
        self.text = self.string()
        self.text = self.leadtrail()
        self.text = self.stopword()


    def stopword(self):
        '''Remove stopwords (english)'''
        out = [word for word in self.text.split() if word not in stopwords()]
        return ' '.join(word for word in out)


    def string(self):
    	'''remove arbitrary string'''
    	return self.text.replace(self.remove_string, '')

    def low(self):
        
        '''make string lowercase'''

        return self.text.lower()

    def caps(self):
        
        '''make string uppercase'''
        
        return self.text.upper()
    
    def punct(self):
        
        '''remove special characters'''
        
        return re.sub('['+string.punctuation+']', '', self.text)
    
    def leadtrail(self):
        
        '''remove trailing and leading whitespace
        
        NOTE: this also removes the last line break'''
        
        return self.text.strip()
    
    def linebreaks(self):
        
        '''remove linebreaks'''

        return self.text.replace('\n', ' ').replace('\r', '')
        
    def decod(self):
        '''decode binary'''
        try:
            return self.text.decode()
        except AttributeError:
            return self.text
        
    def links(self):
        '''remove links'''
        return re.sub(r'http\S+', '', self.text)
        
    def emoji(self):
        
        '''remove emojis'''
    
        emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  
                               u"\U0001F300-\U0001F5FF"  
                               u"\U0001F680-\U0001F6FF"  
                               u"\U0001F1E0-\U0001F1FF" 
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               "]+", flags=re.UNICODE)
        return emoji_pattern.sub(r'', self.text)