def test_clean():

    from signs import Clean

    doc = ' Jack is a green  😂😂😂 cat... \n with a hat \n  '

    # create the object
    cleaned = Clean(doc)

    # access the text
    cleaned.text

    # you could of course also directly do
    Clean(doc).text

    # create the object
    cleaned = Clean(doc, auto=False)

    # make text all caps
    cleaned.caps()

    # make text all lower
    cleaned.low()

    # decode the text
    cleaned.decod()

    # remove emojis
    cleaned.emoji()

    # remove leading and trailing whitespace
    cleaned.leadtrail()

    # remove all whitespace
    cleaned.whitespace()

    # remove linebreaks
    cleaned.linebreaks()

    # remove links
    cleaned.links()

    # remove punctuation
    cleaned.punct()

    # remove arbitrary string
    cleaned.string('is a green')
