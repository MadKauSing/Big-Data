#!/usr/bin/env python3
import sys

print_function=print

path_w_file=sys.argv[1]
path_page_embeddings=sys.argv[2]

#reading files
w_file=open(path_w_file)
page_embed=open(path_page_embeddings)


def calculate_rank():
    #Rank(p) = 0.34 + 0.57 ∑ Contribution of nodes pointing to p
    pass


def calculate_similarity():

    pass


def calculate_contribution():
    
    pass



for line in sys.stdin:
    try:
        temp=line.split()
    except:
        pass
