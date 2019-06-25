def count_consecutive_summers(num):
    count = 1
    i = 1
    while i<num:
        sum = 0
        j=i
        while sum < num:
            sum+=j
            j+=1
        if sum == num:
            count+=1
        i+=1
    return count


if __name__ == '__main__':
    print("Example:")
    print(count_consecutive_summers(42))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert count_consecutive_summers(42) == 4
    assert count_consecutive_summers(99) == 6
    assert count_consecutive_summers(1) == 1
    print("Coding complete? Click 'Check' to earn cool rewards!")
