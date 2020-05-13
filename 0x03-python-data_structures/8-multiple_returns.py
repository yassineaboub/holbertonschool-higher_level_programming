#!/usr/bin/python3
def multiple_returns(sentence):
    first_char = sentence[0]
    if sentence is None or len(sentence) == 0:
        return (len(sentence), None)
    else:
        return (len(sentence), first_char)
