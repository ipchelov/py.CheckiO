VOWELS = "aeiouy"

def translate(phrase):
    str_phrase = ''
    for word in phrase.split():
        long = len(word)
        i=0
        while i < long-1:
            if word[i] in VOWELS:
                word = word[:i+1] + word[i+3:]
                long-=2
            else:
                word = word[:i+1] + word[i+2:]
                long-=1
            i += 1
        str_phrase+= word + ' '
    return str_phrase[:-1]


if __name__ == '__main__':
    print("Example:")
    print(translate("hoooowe yyyooouuu duoooiiine"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
