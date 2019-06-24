def time_converter(time):
    from datetime import datetime
    d = datetime.strptime(time, "%H:%M").strftime("%I:%M %p").replace('PM','p.m.').replace('AM','a.m.')
    if d[0]=='0':
        return d[1:]
    else:
        return d




if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30'))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")
