FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):
    translate = ''
    nums = [int(i) for i in str(number)]
    if len(nums) == 3:
        translate+= FIRST_TEN[nums[0]-1] + ' ' + HUNDRED + ' '
        if nums[1]!=0:
            if nums[1] == 1:
                translate+=SECOND_TEN[nums[2]]
            else:
                translate+=OTHER_TENS[nums[1]-2] + ' '
        if nums[2] != 0 and nums[1] != 1:
            translate+=FIRST_TEN[nums[2]-1]
    elif len(nums) == 2:
        if nums[0]!=1:
            translate+=OTHER_TENS[nums[0]-2] + ' '
            if nums[1]!=0:
                translate+= FIRST_TEN[nums[1] - 1]
        else:
            translate+=SECOND_TEN[nums[1]]
    else:
        translate+=FIRST_TEN[nums[0]-1]


    return translate.strip()

if __name__ == '__main__':

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
    print('Done! Go and Check it!')
