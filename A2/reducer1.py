

curr_word=None

for line in sys.stdin:

    # faster lookups
    try:
        (word, value) = line.split()
        value = int(values.strip())
        
        if curr_word == word:
            print(f", {value}",end="")
        
        else:
            if curr_word:
                print(f"]")
                print(f"[{curr_word}")
                
                curr_word=word
            
            else:
                print(f"[{curr_word}")
                curr_word=word
    
    
    except:
        pass