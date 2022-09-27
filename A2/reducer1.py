import sys
curr_word=None

for line in sys.stdin:
    try:
        (word, value) = line.split()
        value = int(values.strip())
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
