def between_markers(text: str, begin: str, end: str) -> str:
    return text[text.find(begin)+len(begin):text.find(end)]


if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple"
    assert between_markers('What is [apple]', '[', ']') == "apple"
    assert between_markers('What is ><', '>', '<') == ""
    assert between_markers('>apple<', '>', '<') == "apple"
    print('Wow, you are doing pretty good. Time to check it!')

    def popular_words(text: str, words: list) -> dict:
        a = dict()
        for i in words:
            count = 0
            for j in text.split():
                if i == j.lower():
                    count+=1
            a[i]=count
        return a
