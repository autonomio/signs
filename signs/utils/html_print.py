def html_print(text, title=''):

    from IPython.core.display import display, HTML

    # create title for the content
    display(HTML("<h4>" + str(title) + "</h4>"))

    # create content
    html = display(HTML("<font size=2 face=Verdana>" + text + "</font>"))

    return html
