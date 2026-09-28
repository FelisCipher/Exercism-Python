"""Bob's responses"""
def response(hey_bob):
    """Determine the responses of Bob.

    Parameters:
        hey_bob (str): Questions or conversation made with Bob.

    Returns:
        str: Response of Bob.
    """
    convo = hey_bob.strip()
    
    if convo.endswith('?') and convo.isupper():
        return "Calm down, I know what I'm doing!"
    elif convo.endswith('?'):
        return 'Sure.'
    elif convo.isupper():
        return 'Whoa, chill out!'
    elif convo=='':
        return 'Fine. Be that way!'
    else:
        return 'Whatever.'