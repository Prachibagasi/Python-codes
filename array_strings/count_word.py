
def word_count(string):
    """
    Count the number of occurrences of each word in a given string.

    Parameters:
    string (str): The input string to search within.

    Returns:
    dict: A dictionary with words as keys and their occurrence counts as values.
    """
    word_counter = {}
    words = string.split()
    for w in words:
        if w in word_counter:
            word_counter[w]+=1
        else:
            word_counter[w]=1
    return word_counter
# Example usage:
input_string = input("Enter a string: ")    
print(word_count(input_string))
