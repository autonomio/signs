from signs import Clean

def run_test():

	p = Clean(' Jack is a green 😂😂😂 cat... \n with a hat \n  ')

	if p.low() != ' jack is a green 😂😂😂 cat... \n with a hat \n  ': 
	    raise ValueError('low() test failed')
	    
	if p.caps() != ' JACK IS A GREEN 😂😂😂 CAT... \n WITH A HAT \n  ':
	    raise ValueError('caps() test failed')
	    
	if p.punct() != ' Jack is a green 😂😂😂 cat \n with a hat \n  ':
	    raise ValueError('punct() test failed')
	    
	if p.leadtrail() != 'Jack is a green 😂😂😂 cat... \n with a hat':
	    raise ValueError('leadtrail() test failed')
	    
	if p.linebreaks() != ' Jack is a green 😂😂😂 cat...   with a hat    ':
	    raise ValueError('linebreaks() test failed')
	    
	if p.emoji() != ' Jack is a green  cat... \n with a hat \n  ':
	    raise ValueError('linebreaks() test failed')
