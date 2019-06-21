def between_markers(text: str, begin:str, end:str) -> str:
    begin_f = text.find(begin)
    end_f = text.find(end)
    if begin_f>-1 and end_f>-1:
        if begin_f>end_f:
            return ""
        else:
            return text[begin_f+len(begin):end_f]
    elif begin_f>-1 and end_f==-1:
        return text[begin_f+len(begin):]
    elif begin_f==-1 and end_f>-1:
        return text[:end_f]
    else:
        return text


if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')
