import string
def is_pangram(sentence):
    """
    Checks if the given sentence is a pangram
    
    Param:
    sentence (str): Sentence to be checked
    
    Returns: boolean
    """
    alphabets = set(string.ascii_lowercase)
    test_set = set(sentence.lower())

    test_set.difference_update(test_set.difference(alphabets))
    
    return len(test_set)==len(alphabets)
