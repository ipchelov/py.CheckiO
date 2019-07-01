def checkio(n):
    ones = ["","I","II","III","IV","V","VI","VII","VIII","IX"]
    tens = ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
    hunds = ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
    thous = ["","M","MM","MMM","MMMM"]

    t = thous[n//1000]
    h = hunds[n//100%10]
    te = tens[n//10%10]
    o = ones[n%10]
    return t + h + te + o


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print(checkio(113))
    # assert checkio(6) == 'VI', '6'
    # assert checkio(76) == 'LXXVI', '76'
    # assert checkio(499) == 'CDXCIX', '499'
    # assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
    print('Done! Go Check!')
