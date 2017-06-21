
def hey(what):
    if what.isupper():
        return 'Whoa, chill out!'
    elif what.rstrip().endswith('?'):
        return 'Sure.'
    elif what.strip() == '':
        return 'Fine. Be that way!'
    else:
        return 'Whatever.'
