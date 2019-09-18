#!/usr/bin/python3
def multiple_returns(sentence):
    len_sen = len(sentence)
    if (len_sen != 0):
        tuple = (len_sen, sentence[0])
    else:
        tuple = (len_sen, None)
    return (tuple)
