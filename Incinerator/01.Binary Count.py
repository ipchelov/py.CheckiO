def checkio(number: int) -> int:
    bin = ''
    while number > 0:
        bin += str(number % 2)
        number=number//2
    return bin.count('1')

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4) == 1
    assert checkio(15) == 4
    assert checkio(1) == 1
    assert checkio(1022) == 9
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
