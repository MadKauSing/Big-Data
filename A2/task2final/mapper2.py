#!/usr/bin/env python3
import sys,json,re


#*************SHORTCUTS TO FUNCTIONS****************
# Shortcut to functions
print_function=print
len_function=len
#***************************************************

#*****************READING ARGUMENTS*****************
path_w_file=sys.argv[1]
path_page_embeddings=sys.argv[2]
#**************************************************


#*****************Reading Files********************
w_file=open(path_w_file)
page_embed=open(path_page_embeddings)
page_embed_dic=json.load(page_embed)
dic = {}
#**************************************************
for i in page_embed_dic.keys():
    dic[i]=0



def help_multiply_vectors(x,y,kernel_size=6):
    n1=len_function(x)
    n2=len_function(y)

    if n1!=n2: return -1

    else:
        s=0
        i=0
        boundary=n1-kernel_size-1
        while i < boundary:
            s+=x[i]*y[i]
            s+=x[i+1]*y[i+1]
            s+=x[i+2]*y[i+2]
            s+=x[i+3]*y[i+3]
            s+=x[i+4]*y[i+4]
            s+=x[i+5]*y[i+5]
            i+=kernel_size
        while i < n1:
            s+=x[i] * y[i]
            i+=1
        # print(s)
        return s

def calculate_similarity(p,q,cache):
    dot_product = help_multiply_vectors(p,q)
    if cache is None:
        # Compute Dot product, Norms of p and q using loop unrolling. 
        # (Note you can compute everything in one loop unrolling segment).
        # norm_p = (p[0]**2 + p[1]**2 + p[2]**2 + p[3]**2 + p[4]**2 + p[5]**2)**(1/2)
        norm_p = help_multiply_vectors(p,p)
        norm_q = help_multiply_vectors(q,q)
        cache = norm_p
        similarity = (dot_product)/(norm_p + norm_q - dot_product)
    else:
        norm_q = help_multiply_vectors(q,q)
        # Compute Dot product, Norm of q using loop unrolling. 
        # (Note you can compute everything in one loop unrolling segment).
        similarity = dot_product/(cache + norm_q - dot_product)
    return similarity, cache


def calculate_contribution(p,q,no_out,r_dash,p_cache):
    similarity,p_cache=calculate_similarity(p,q,p_cache)  
    contribution=similarity*(r_dash/no_out)
    return contribution,p_cache



# adjancency list from sys.stdin
# ranks form w file
for line in sys.stdin:
    #reading page_rank file
    w_node,w_rank=w_file.readline().split(',')
    w_rank=w_rank.strip()
    
    #reading adjacency
    node,node_outgoing = line.split('\t')
    
    node_outgoing=re.sub(r'[^\w]', ' ', node_outgoing).split()
    # print(node,node_outgoing)
    # print(w_node,w_rank)
    cache=None
    for i in node_outgoing:
        contribution, cache = calculate_contribution(page_embed_dic[str(node)],page_embed_dic[str(i)],len(page_embed_dic[str(i)]),int(w_rank),cache)
        print(i,contribution)
        if dic[i]==0:
            dic[i]=1

for i in dic:
    if dic[i]==0:
        print(i,float(0))

# print(calculate_similarity(page_embed_dic['1'],page_embed_dic['2'],None))
# print(calculate_contribution(page_embed_dic['1'],page_embed_dic['2'],2,1,None))



#output should be p contiribution
# p con
# p con1
# p con2