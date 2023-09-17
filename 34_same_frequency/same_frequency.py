def counter(num):
    """
    Returns a dict containing the frequency of 
    each number
    """
    
    freq = {}
    
    for x in str(num):
        freq[x] = freq.get(x, 0) + 1
        
    return freq


def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """

    return (counter(num1) == counter(num2))