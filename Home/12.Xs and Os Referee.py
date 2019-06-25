from typing import List

def checkio(game_result: List[str]) -> str:
    a = game_result
    for i in range(3):
        if a[0][i]==a[1][i]==a[2][i] and a[0][i]!='.':
            return a[0][i]
        if a[i][0]==a[i][1]==a[i][2] and a[i][0]!='.':
            return a[i][0]
    if (a[0][0]==a[1][1]==a[2][2] or a[0][2]==a[1][1]==a[2][0]) and a[1][1]!='.':
        return a[1][1]

    return "D"



if __name__ == '__main__':
    print("Example:")
    print(checkio(["X.O",
                   "XX.",
                   "XOO"]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
