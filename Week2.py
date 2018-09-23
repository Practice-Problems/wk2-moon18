#Moonis Rasheed
#Week 2 Programming Practice

import math

#Question-1 Sherlock and Squares

##def squares(a, b):
##    num_squares=0
##    if a<=1 or b<=1:
##        return 0
##    else:
##        for i in range(a,b+1):
##            for j in range((i/2)+1):
##                if (j*j)==i:
##                    num_squares=num_squares+1
##        return num_squares
def squares(a,b):
    high_limit=math.floor(math.sqrt(b))
    lower_limit=math.ceil(math.sqrt(a))
    return high_limit-(lower_limit+1)

#Question-2 Encryption

def encryption(s):
    sentence=s.replace(" ","")
    sen_list=[]
    limit=math.sqrt(len(sentence))
    row=math.floor(limit) 
    col=math.ceil(limit)
    for i in range(col):
        string=""
        for j in range(i,len(sentence),col):
            string+=sentence[j]
        sen_list.append(string)
    return(' '.join(sen_list))

##def encryption(s):
##    sentence=s.replace(' ', '')
##    sentence_size=len(sentence)
##    lowerbound = math.floor(math.sqrt(sentence_size))
##    upperbound = math.ceil(math.sqrt(sentence_size))
##    total = upperbound * lowerbound
##    sen_list=[]
##    encrypt=""
##    while (total < sentence_size):
##        if (lowerbound < upperbound):
##            lowerbound+=1
##        else: 
##            upperbound+=1
##    
##        total = upperbound * lowerbound
##    for i in range(0,lowerbound):
##        for j in range(0,upperbound):
##            #if (index <= len(s) - 1):
##            sen_list.append([i,j])
##            
##    for i in range(0, upperbound):
##        for j in range(0, lowerbound):
##            if (sen_list[i][j] != 0):
##                encrypt+= sen_list[i][j]
##        
####    if (col != upperbound - 1):
####        encrypt+= " "
##    return encrypt


  
            
            
            
