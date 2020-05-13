#!/usr/bin/python3
def multiple_returns(sentence):
    first_char = sentence[0]
    if sentence == "":
        return None
    else:
            return (len(sentence), first_char)
