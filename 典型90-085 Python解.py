#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from math import ceil
def make_divisors(n):
    lo,hi = [],[]
    i = 1
    while i*i <= n:
        if n%i == 0:
            lo.append(i)
            if i != n // i:
                hi.append(n//i)
        i += 1
    return lo + hi[::-1]
K = int(input())
S = make_divisors(K)

#print(S)
ans = 0
#ans  a = 1 の場合のb,cの組の個数
ans += ceil(len(S) / 2)
ans_2 = 0
#ans_2 a >= 2の場合のb,cの組の個数
for i in range(1,len(S)):
    # S[i] = a
    for j in range(1,len(S)):
        # S[j] = b
        if S[i] * S[j] > K:
            # S[i] * S[j] > Kの場合 cは存在しない
            break
        if K % (S[i] * S[j]) == 0:
            T = K // (S[i]*S[j])
            #T = c
            if S[i] <= S[j] <= T:
                #関係を確かめている
                ans_2 += 1
print(ans + ans_2)
#答えの合計を計算している

