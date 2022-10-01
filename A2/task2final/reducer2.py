#!/usr/bin/env python3
import sys

# To run this
# cat test.txt | python3 mapper1.py | python3 reducer1.py w.txt >output.txt

curr_word=None
curr_sum=0
float_function=float


def stringIsEqual(word1,word2):
    if word1==word2:
        return True
    else:
        return False



for line in sys.stdin:
    try:
        word, value = line.split()
        value = float_function(value.strip())
    except:
        pass
    if curr_word == word:
        curr_sum+=value
    else:
        if curr_word:
            rank=0.34+0.57*curr_sum
            print(f"{curr_word},{'%0.2f' % rank}")
            
            curr_word=word
            curr_sum=value
        else:
            curr_word=word
            curr_sum+=value
            
rank=0.34+0.57*curr_sum
print(f"{curr_word},{'%0.2f' % rank}")


