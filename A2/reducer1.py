#!/usr/bin/env python3
import sys

path_to_file = sys.argv[1]

curr_word=None
int_function=int


def stringIsEqual(word1,word2):
    if word1==word2:
        return True
    else:
        return False

fob=open(path_to_file,'w')

for line in sys.stdin:
    try:
        (word, value) = line.split()
        value = int_function(values.strip())
    except:
        pass
    if curr_word == word:
        print(f", {value}",end="")
    else:
        if curr_word:
            print(f"]")
            curr_word=word
            fob.write(f"{curr_word},1\n")
            print(f"{curr_word}\t[{value}",end="")
        else:
            curr_word=word
            fob.write(f"{curr_word},1\n")
            print(f"{curr_word}\t[{value}",end="")
print("]")
