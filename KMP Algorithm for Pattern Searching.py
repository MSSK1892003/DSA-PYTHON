
def KMPAlgo(P,S):
    M=len(P)
    N=len(S)
    lps=[]
    LPS(P,M,lps)
    print(lps)
    i=0
    j=0
    while (N-i)>=(M-j):
        if P[j]==S[i]:
            i+=1
            j+=1
            
        if j == M:
            print("Pattern Found",i-j)
            j=lps[j-1]
        elif i<N and P[j]!=S[i]:
            if j!=0:
                j=lps[j-1]
            else:
                i+=1
def LPS(P,M,lps):
   len=0
   lps.append(0)
   i=1
   while i<M:
       if P[i]==P[len]:
           len+=1
           lps.append(len)
           i+=1
       else:
           if len!=0:
               len=lps[len-1]
           else:
               lps.append(i)
               i+=1
   
            
if __name__=="__main__":
    # S="ABABACDEABABABCABCABCABDAA"
    S="ABABDABACDABABCABAB"
    # P="ABCAB"
    P="ABABCABAB"
    KMPAlgo(P,S)