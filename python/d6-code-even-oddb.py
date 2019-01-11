#!/bin/python3

""" Print letters at even index locations followed by
    letter at odd index locations
"""
if __name__ == '__main__':

    for n in range(int(input())):
        s = input()
        print(s[::2], s[1::2])
