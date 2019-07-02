def verify_anagrams(first_word, second_word):
    longest = first_word if len(first_word) > len(second_word) else second_word
    for i in longest.lower():
        if first_word.lower().count(i)!=second_word.lower().count(i) \
                and i!=' ':
            return False
    return True

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(verify_anagrams("a", 'z'), bool), "Boolean!"
    assert verify_anagrams("Programming", "Gram Ring Mop") == True, "Gram of code"
    assert verify_anagrams("Hello", "Ole Oh") == False, "Hello! Ole Oh!"
    assert verify_anagrams("Kyoto", "Tokyo") == True, "The global warming crisis of 3002"

