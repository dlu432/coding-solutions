#!/bin/python3

""" Print letters at even index locations followed by
    letter at odd index locations
"""
if __name__ == '__main__':
    num_tests = int(input())
    tests = []
    for i in range(num_tests):
        tests.append(input())

    for word in tests:
        for i in range (0,len(word),2):
            print(word[i],end="")

        print(" ",end="")
        for j in range (1,len(word),2):
                print(word[j],end="")
        print("")
