def read_file(filename):

    '''Takes as input a file where each row will become
    a document in the output list

    filename : str
        Local file with content

    '''

    with open(filename) as f:
        content = f.readlines()

    content = [x for x in content]

    return content
