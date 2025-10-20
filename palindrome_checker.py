def is_palindrome(word):
    """
    Check if a word is a palindrome.
    
    A palindrome is a word that reads the same forwards and backwards.
    The function is case-insensitive and ignores non-alphabetic characters.
    
    Args:
        word (str): The word to check
        
    Returns:
        bool: True if the word is a palindrome, False otherwise
        
    Examples:
        >>> is_palindrome("racecar")
        True
        >>> is_palindrome("hello")
        False
        >>> is_palindrome("A man a plan a canal Panama")
        True
        >>> is_palindrome("Madam")
        True
    """
    # Convert to lowercase and remove non-alphabetic characters
    cleaned = ''.join(char.lower() for char in word if char.isalnum())
    
    # Check if the cleaned string is equal to its reverse
    return cleaned == cleaned[::-1]
