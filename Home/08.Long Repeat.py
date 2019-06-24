def long_repeat(line):
    max = 1
    last_max = 1
    if len(line) == 0:
        return 0
    for i in range(len(line)-1):
        if line[i]==line[i+1]:
            last_max+=1
            if last_max > max:
                max = last_max
        else:last_max = 1
    return max

if __name__ == '__main__':
    print(long_repeat('aa'))
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')
