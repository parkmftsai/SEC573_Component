def table(s):
    j=0
    table=[0]
    for i in range(1,len(s),+1):
        while(j>0 and s[j]!=s[i]):
             j=table[j-1]
        if(s[j]==s[i]):
           j+=1
        table.append(j)
    return table



def KMP(s,m):
    a=len(s)
    b=len(m)
    i=0
    _table=table(m)
    print(_table)
    while(i<a):        
	for j in range(0,b,+1):
            if(s[i+j]!=m[j]):
               i+=max((j-_table[j-1]),1)
               break
        else:
           return True
    return False     



print(KMP("BBC ABCDAB ABCDABCDABDE","ABCDABF"))
