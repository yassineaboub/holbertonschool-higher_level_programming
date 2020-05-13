#!/usr/bin/python3
def multiple_returns(sentence):
    first_char = sentence[0]
    if len(sentence) == 0:
        return first_char is None
    else:
        return (len(sentence), first_char)
