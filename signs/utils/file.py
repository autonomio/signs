def read_file(filename):
    
    '''Read text from a file'''

    with open(filename) as f:
        content = f.readlines()
        
    content = [x for x in content] 
        
    return content