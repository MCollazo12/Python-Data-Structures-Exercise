def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    
    VOWELS = 'aeiouAEIOU' 
    string = list(s)
    
    left, right = 0, len(string) - 1
    
    while left < right:
        # Find the next vowel from the left
        while left < right and string[left] not in VOWELS:
            left += 1
        
        # Find the next vowel from the right
        while left < right and string[right] not in VOWELS:
            right -= 1
        
        # Swap the vowels
        string[left], string[right] = string[right], string[left]
        
        left += 1
        right -= 1
    
    # Convert the list back to a string
    result = ''.join(string)
    
    return result

reverse_vowels("Tomatoes")