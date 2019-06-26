def checkio(expression):
    open_br = '{(['
    close_br = '})]'
    new_exp = ''
    stack = []
    for i in expression:
        if i in open_br or i in close_br:
            new_exp+= i
    if len(new_exp) == 0:
        return True
    if new_exp[0] in close_br or len(new_exp)%2==1:
        return False
    else:
        for i in new_exp:
            if i in open_br:
                stack.append(i)
            elif open_br.find(stack.pop())==close_br.find(i):
                continue
            else:
                return False
    return True


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"
