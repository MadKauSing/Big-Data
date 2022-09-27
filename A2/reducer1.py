import sys
curr_word=None
int_function=int

def stringIsEqual(word1,word2):
    if word1==word2:
        return True
    else:
        return False


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
            print(f"{curr_word}\t[{value}",end="")
        else:
            curr_word=word
            print(f"{curr_word}\t[{value}",end="")
print("]")
