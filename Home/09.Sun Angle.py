def sun_angle(time):
    first = int(time[0:2])
    second = int(time[3:])
    if first < 6 or (first >= 18 and second > 0):
        return "I don't see the sun!"
    else:
        return ((first-6) * 60 + second)/720 * 180

if __name__ == '__main__':
    print("Example:")
    print(sun_angle("18:01"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
