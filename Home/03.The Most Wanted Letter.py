def checkio(text: str) -> str:
    new_text = ''.join(filter(str.isalpha,text)).lower()
    addlist = []
    my_d = {x:new_text.count(x) for x in new_text}
    maxim = max(my_d.values())
    if list(my_d.values()).count(maxim) == 1 :
        for k, v in my_d.items():
            if v == maxim:
                return k
    else:
        for k,v in my_d.items():
            if v==maxim:
                addlist.append(k)
        return sorted(addlist)[0]



if __name__ == '__main__':
    print("Example:")
    print(checkio("One"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
