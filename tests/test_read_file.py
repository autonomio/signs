def test_read_file():

    from signs.utils.file import read_file

    s = "here is test \n that goes into a file \n"
    f = open('temp.txt', 'w')
    f.write(s)
    f.close()

    out = read_file('temp.txt')
    if out != ['here is test \n', ' that goes into a file \n']:
        raise ValueError('read_file() test failed')
