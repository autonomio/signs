import re
import string

class Clean:
    
    def __init__(self, text):
        
        self.text = text
        
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