def calc_max(p,w,c,n):
    if n==0 or c==0:
        return 0
    if Dp[n][c]!=-1:
        return Dp[n][c]
    if (w[n-1]<=c):
        Dp[n][c]= max(p[n-1]+calc_max(p,w,c-w[n-1],n-1),calc_max(p,w,c,n-1))
        return Dp[n][c]
    else:
        Dp[n][c]=calc_max(p,w,c,n-1)
        return Dp[n][c]
p=[5,10,15,7,8,9,4]
w=[1,3,5,4,1,3,2]
c=15
n=len(p)
Dp=[[-1 for i in range  (c+1)] for j in range(n+1)]

print(calc_max(p,w,c,n))
print(Dp)