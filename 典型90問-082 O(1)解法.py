#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#a以上b以下の数の「文字数」の計算
#ひとこと：
#累積和を使えばこういうコードは短くなる、という典型例
def num(a,b,c):
    #aが左端,bが右端,cが個数
    X = b * (b + 1)//2
    Y = (a - 1) * a //2
    return (X-Y)*c

L,R = map(int,input().split())
ans = 0
ls = []
#あらかじめ計算しておく
for i in range(18):
    ls.append(num(10**(i),10**(i+1)-1,i+1))
if R<10:
    ans+=num(L,R,1) 
elif R<100:
    if L<10:
        ans+=num(L,9,1)
        ans+=num(10,R,2)
    else:
        ans+=num(L,R,2)
elif R<10**3:
    if L<10:
        ans+=num(L,9,1)
        ans+=ls[1]
        ans+=num(100,R,3)
    elif L<100:
        ans+=num(L,99,2)
        ans+=num(100,R,3)
    else:
        ans +=num(L,R,3)
elif R<10**4:
    if L<10:
        ans+=num(L,9,1)
        ans+=ls[1]
        ans+=ls[2]
        ans+=num(1000,R,4)
    elif L<100:
        ans+=num(L,99,2)
        ans+=ls[2]
        ans+=num(1000,R,4)
    elif L<1000:
        ans+=num(L,999,3)
        ans+=num(1000,R,4)
    else:
        ans+=num(L,R,4)
elif R<10**5:
    if L<10:
        ans+=num(L,9,1)
        ans+=ls[1]
        ans+=ls[2]
        ans+=ls[3]
        ans+=num(10000,R,5)
    elif L<100:
        ans+=num(L,99,2)
        ans+=ls[2]
        ans+=ls[3]
        ans+=num(10000,R,5)
    elif L<1000:
        ans+=num(L,999,3)
        ans+=ls[3]
        ans+=num(10000,R,5)
    elif L<10000:
        ans +=num(L,9999,4)
        ans +=num(10000,R,5)
    else:
        ans +=num(L,R,5)
elif R < 10 ** 6:
    if L<10:
        ans+=num(L,9,1)
        ans+=ls[1]
        ans+=ls[2]
        ans+=ls[3]
        ans+=ls[4]
        ans+=num(10**5,R,6)
    elif L<10**2:
        ans+=num(L,99,2)
        ans+=ls[2]
        ans+=ls[3]
        ans+=ls[4]
        ans+=num(10**5,R,6)
    elif L<10**3:
        ans+=num(L,999,3)
        ans+=ls[3]
        ans+=ls[4]
        ans+=num(10**5,R,6)
    elif L<10**4:
        ans+=num(L,9999,4)
        ans+=ls[4]
        ans+=num(10**5,R,6)
    elif L<10**5:
        ans+=num(L,99999,5)
        ans+=num(10**5,R,6)
    else:
        ans+=num(L,R,6)
elif R < 10 ** 7:
    if L<10:
        ans+=num(L,9,1)
        ans+=ls[1]
        ans+=ls[2]
        ans+=ls[3]
        ans+=ls[4]
        ans+=ls[5]
        ans+=num(10**6,R,7)
    elif L<100:
        ans+=num(L,99,2)
        ans+=ls[2]
        ans+=ls[3]
        ans+=ls[4]
        ans+=ls[5]
        ans+=num(10**6,R,7)
    elif L<1000:
        ans+=num(L,999,3)
        ans+=ls[3]
        ans+=ls[4]
        ans+=ls[5]
        ans+=num(10**6,R,7)
    elif L<10**4:
        ans+=num(L,9999,4)
        ans+=ls[4]
        ans+=ls[5]
        ans+=num(10**6,R,7)
    elif L<10**5:
        ans+=num(L,99999,5)
        ans+=ls[5]
        ans+=num(10**6,R,7)
    elif L<10**6:
        ans+=num(L,10**6-1,6)
        ans+=num(10**6,R,7)
    else:
        ans+=num(L,R,7)
elif R < 10 ** 8:
    if L<10:
        ans+=num(L,9,1)
        ans+=ls[1]
        ans+=ls[2]
        ans+=ls[3]
        ans+=ls[4]
        ans+=ls[5]
        ans+=ls[6]
        ans+=num(10**7,R,8)
    elif L<100:
        ans+=num(L,99,2)
        ans+=ls[2]
        ans+=ls[3]
        ans+=ls[4]
        ans+=ls[5]
        ans+=ls[6]
        ans+=num(10**7,R,8)
    elif L<1000:
        ans+=num(L,999,3)
        ans+=ls[3]
        ans+=ls[4]
        ans+=ls[5]
        ans+=ls[6]
        ans+=num(10**7,R,8)
    elif L<10**4:
        ans+=num(L,9999,4)
        ans+=ls[4]
        ans+=ls[5]
        ans+=ls[6]
        ans+=num(10**7,R,8)
    elif L<10**5:
        ans+=num(L,99999,5)
        ans+=ls[5]
        ans+=ls[6]
        ans+=num(10**7,R,8)
    elif L<10**6:
        ans+=num(L,10**6-1,6)
        ans+=ls[6]
        ans+=num(10**7,R,8)
    elif L<10**7:
        ans+=num(L,10**7-1,7)
        ans+=num(10**7,R,8)
    else:
        ans+=num(L,R,8)
elif R < 10 ** 9:
    if L<10:
        ans+=num(L,9,1)
        ans+=ls[1]
        ans+=ls[2]
        ans+=ls[3]
        ans+=ls[4]
        ans+=ls[5]
        ans+=ls[6]
        ans+=ls[7]
        ans+=num(10**8,R,9)
    elif L<100:
        ans+=num(L,99,2)
        ans+=ls[2]
        ans+=ls[3]
        ans+=ls[4]
        ans+=ls[5]
        ans+=ls[6]
        ans+=ls[7]
        ans+=num(10**8,R,9)
    elif L<1000:
        ans+=num(L,999,3)
        ans+=ls[3]
        ans+=ls[4]
        ans+=ls[5]
        ans+=ls[6]
        ans+=ls[7]
        ans+=num(10**8,R,9)
    elif L<10**4:
        ans+=num(L,9999,4)
        ans+=ls[4]
        ans+=ls[5]
        ans+=ls[6]
        ans+=ls[7]
        ans+=num(10**8,R,9)
    elif L<10**5:
        ans+=num(L,99999,5)
        ans+=ls[5]
        ans+=ls[6]
        ans+=ls[7]
        ans+=num(10**8,R,9)
    elif L<10**6:
        ans+=num(L,10**6-1,6)
        ans+=ls[6]
        ans+=ls[7]
        ans+=num(10**8,R,9)
    elif L<10**7:
        ans+=num(L,10**7-1,7)
        ans+=ls[7]
        ans+=num(10**8,R,9)
    elif L<10**8:
        ans+=num(L,10**8-1,8)
        ans+=num(10**8,R,9)
    else:
        ans+=num(L,R,9)
elif R < 10 ** 10:
    if L<10:
        ans+=num(L,9,1)
        ans+=ls[1]
        ans+=ls[2]
        ans+=ls[3]
        ans+=ls[4]
        ans+=ls[5]
        ans+=ls[6]
        ans+=ls[7]
        ans+=ls[8]
        ans+=num(10**9,R,10)
    elif L<100:
        ans+=num(L,99,2)
        ans+=ls[2]
        ans+=ls[3]
        ans+=ls[4]
        ans+=ls[5]
        ans+=ls[6]
        ans+=ls[7]
        ans+=ls[8]
        ans+=num(10**9,R,10)
    elif L<1000:
        ans+=num(L,999,3)
        ans+=ls[3]
        ans+=ls[4]
        ans+=ls[5]
        ans+=ls[6]
        ans+=ls[7]
        ans+=ls[8]
        ans+=num(10**9,R,10)
    elif L<10**4:
        ans+=num(L,9999,4)
        ans+=ls[4]
        ans+=ls[5]
        ans+=ls[6]
        ans+=ls[7]
        ans+=ls[8]
        ans+=num(10**9,R,10)
    elif L<10**5:
        ans+=num(L,99999,5)
        ans+=ls[5]
        ans+=ls[6]
        ans+=ls[7]
        ans+=ls[8]
        ans+=num(10**9,R,10)
    elif L<10**6:
        ans+=num(L,10**6-1,6)
        ans+=ls[6]
        ans+=ls[7]
        ans+=ls[8]
        ans+=num(10**9,R,10)
    elif L<10**7:
        ans+=num(L,10**7-1,7)
        ans+=ls[7]
        ans+=ls[8]
        ans+=num(10**9,R,10)
    elif L<10**8:
        ans+=num(L,10**8-1,8)
        ans+=ls[8]
        ans+=num(10**9,R,10)
    elif L<10**9:
        ans+=num(L,10**9-1,9)
        ans+=num(10**9,R,10)
    else:
        ans+=num(L,R,10)
elif R < 10 ** 11:
    if L<10:
        ans+=num(L,9,1)
        ans+=ls[1]
        ans+=ls[2]
        ans+=ls[3]
        ans+=ls[4]
        ans+=ls[5]
        ans+=ls[6]
        ans+=ls[7]
        ans+=ls[8]
        ans+=ls[9]
        ans+=num(10**10,R,11)
    elif L<100:
        ans+=num(L,99,2)
        ans+=ls[2]
        ans+=ls[3]
        ans+=ls[4]
        ans+=ls[5]
        ans+=ls[6]
        ans+=ls[7]
        ans+=ls[8]
        ans+=ls[9]
        ans+=num(10**10,R,11)
    elif L<1000:
        ans+=num(L,999,3)
        ans+=ls[3]
        ans+=ls[4]
        ans+=ls[5]
        ans+=ls[6]
        ans+=ls[7]
        ans+=ls[8]
        ans+=ls[9]
        ans+=num(10**10,R,11)
    elif L<10**4:
        ans+=num(L,9999,4)
        ans+=ls[4]
        ans+=ls[5]
        ans+=ls[6]
        ans+=ls[7]
        ans+=ls[8]
        ans+=ls[9]
        ans+=num(10**10,R,11)
    elif L<10**5:
        ans+=num(L,99999,5)
        ans+=ls[5]
        ans+=ls[6]
        ans+=ls[7]
        ans+=ls[8]
        ans+=ls[9]
        ans+=num(10**10,R,11)
    elif L<10**6:
        ans+=num(L,10**6-1,6)
        ans+=ls[6]
        ans+=ls[7]
        ans+=ls[8]
        ans+=ls[9]
        ans+=num(10**10,R,11)
    elif L<10**7:
        ans+=num(L,10**7-1,7)
        ans+=ls[7]
        ans+=ls[8]
        ans+=ls[9]
        ans+=num(10**10,R,11)
    elif L<10**8:
        ans+=num(L,10**8-1,8)
        ans+=ls[8]
        ans+=ls[9]
        ans+=num(10**10,R,11)
    elif L<10**9:
        ans+=num(L,10**9-1,9)
        ans+=ls[9]
        ans+=num(10**10,R,11)
    elif L<10**10:
        ans+=num(L,10**10-1,10)
        ans+=num(10**10,R,11)
    else:
        ans+=num(L,R,11)
elif R < 10 ** 12:
    if L<10:
        ans+=num(L,9,1)
        ans+=ls[1]
        ans+=ls[2]
        ans+=ls[3]
        ans+=ls[4]
        ans+=ls[5]
        ans+=ls[6]
        ans+=ls[7]
        ans+=ls[8]
        ans+=ls[9]
        ans+=ls[10]
        ans+=num(10**11,R,12)
    elif L<100:
        ans+=num(L,99,2)
        ans+=ls[2]
        ans+=ls[3]
        ans+=ls[4]
        ans+=ls[5]
        ans+=ls[6]
        ans+=ls[7]
        ans+=ls[8]
        ans+=ls[9]
        ans+=ls[10]
        ans+=num(10**11,R,12)
    elif L<1000:
        ans+=num(L,999,3)
        ans+=ls[3]
        ans+=ls[4]
        ans+=ls[5]
        ans+=ls[6]
        ans+=ls[7]
        ans+=ls[8]
        ans+=ls[9]
        ans+=ls[10]
        ans+=num(10**11,R,12)
    elif L<10**4:
        ans+=num(L,9999,4)
        ans+=ls[4]
        ans+=ls[5]
        ans+=ls[6]
        ans+=ls[7]
        ans+=ls[8]
        ans+=ls[9]
        ans+=ls[10]
        ans+=num(10**11,R,12)
    elif L<10**5:
        ans+=num(L,99999,5)
        ans+=ls[5]
        ans+=ls[6]
        ans+=ls[7]
        ans+=ls[8]
        ans+=ls[9]
        ans+=ls[10]
        ans+=num(10**11,R,12)
    elif L<10**6:
        ans+=num(L,10**6-1,6)
        ans+=ls[6]
        ans+=ls[7]
        ans+=ls[8]
        ans+=ls[9]
        ans+=ls[10]
        ans+=num(10**11,R,12)
    elif L<10**7:
        ans+=num(L,10**7-1,7)
        ans+=ls[7]
        ans+=ls[8]
        ans+=ls[9]
        ans+=ls[10]
        ans+=num(10**11,R,12)
    elif L<10**8:
        ans+=num(L,10**8-1,8)
        ans+=ls[8]
        ans+=ls[9]
        ans+=ls[10]
        ans+=num(10**11,R,12)
    elif L<10**9:
        ans+=num(L,10**9-1,9)
        ans+=ls[9]
        ans+=ls[10]
        ans+=num(10**11,R,12)
    elif L<10**10:
        ans+=num(L,10**10-1,10)
        ans+=ls[10]
        ans+=num(10**11,R,12)
    elif L<10**11:
        ans+=num(L,10**11-1,11)
        ans+=num(10**11,R,12)
    else:
        ans+=num(L,R,12)
elif R < 10 ** 13:
    if L<10:
        ans+=num(L,9,1)
        ans+=ls[1]
        ans+=ls[2]
        ans+=ls[3]
        ans+=ls[4]
        ans+=ls[5]
        ans+=ls[6]
        ans+=ls[7]
        ans+=ls[8]
        ans+=ls[9]
        ans+=ls[10]
        ans+=ls[11]
        ans+=num(10**12,R,13)
    elif L<100:
        ans+=num(L,99,2)
        ans+=ls[2]
        ans+=ls[3]
        ans+=ls[4]
        ans+=ls[5]
        ans+=ls[6]
        ans+=ls[7]
        ans+=ls[8]
        ans+=ls[9]
        ans+=ls[10]
        ans+=ls[11]
        ans+=num(10**12,R,13)
    elif L<1000:
        ans+=num(L,999,3)
        ans+=ls[3]
        ans+=ls[4]
        ans+=ls[5]
        ans+=ls[6]
        ans+=ls[7]
        ans+=ls[8]
        ans+=ls[9]
        ans+=ls[10]
        ans+=ls[11]
        ans+=num(10**12,R,13)
    elif L<10**4:
        ans+=num(L,9999,4)
        ans+=ls[4]
        ans+=ls[5]
        ans+=ls[6]
        ans+=ls[7]
        ans+=ls[8]
        ans+=ls[9]
        ans+=ls[10]
        ans+=ls[11]
        ans+=num(10**12,R,13)
    elif L<10**5:
        ans+=num(L,99999,5)
        ans+=ls[5]
        ans+=ls[6]
        ans+=ls[7]
        ans+=ls[8]
        ans+=ls[9]
        ans+=ls[10]
        ans+=ls[11]
        ans+=num(10**12,R,13)
    elif L<10**6:
        ans+=num(L,10**6-1,6)
        ans+=ls[6]
        ans+=ls[7]
        ans+=ls[8]
        ans+=ls[9]
        ans+=ls[10]
        ans+=ls[11]
        ans+=num(10**12,R,13)
    elif L<10**7:
        ans+=num(L,10**7-1,7)
        ans+=ls[7]
        ans+=ls[8]
        ans+=ls[9]
        ans+=ls[10]
        ans+=ls[11]
        ans+=num(10**12,R,13)
    elif L<10**8:
        ans+=num(L,10**8-1,8)
        ans+=ls[8]
        ans+=ls[9]
        ans+=ls[10]
        ans+=ls[11]
        ans+=num(10**12,R,13)
    elif L<10**9:
        ans+=num(L,10**9-1,9)
        ans+=ls[9]
        ans+=ls[10]
        ans+=ls[11]
        ans+=num(10**12,R,13)
    elif L<10**10:
        ans+=num(L,10**10-1,10)
        ans+=ls[10]
        ans+=ls[11]
        ans+=num(10**12,R,13)
    elif L<10**11:
        ans+=num(L,10**11-1,11)
        ans+=ls[11]
        ans+=num(10**12,R,13)
    elif L<10**12:
        ans+=num(L,10**12-1,12)
        ans+=num(10**12,R,13)
    else:
        ans+=num(L,R,13)
elif R < 10 ** 14:
    if L<10:
        ans+=num(L,9,1)
        ans+=ls[1]
        ans+=ls[2]
        ans+=ls[3]
        ans+=ls[4]
        ans+=ls[5]
        ans+=ls[6]
        ans+=ls[7]
        ans+=ls[8]
        ans+=ls[9]
        ans+=ls[10]
        ans+=ls[11]
        ans+=ls[12]
        ans+=num(10**13,R,14)
    elif L<100:
        ans+=num(L,99,2)
        ans+=ls[2]
        ans+=ls[3]
        ans+=ls[4]
        ans+=ls[5]
        ans+=ls[6]
        ans+=ls[7]
        ans+=ls[8]
        ans+=ls[9]
        ans+=ls[10]
        ans+=ls[11]
        ans+=ls[12]
        ans+=num(10**13,R,14)
    elif L<1000:
        ans+=num(L,999,3)
        ans+=ls[3]
        ans+=ls[4]
        ans+=ls[5]
        ans+=ls[6]
        ans+=ls[7]
        ans+=ls[8]
        ans+=ls[9]
        ans+=ls[10]
        ans+=ls[11]
        ans+=ls[12]
        ans+=num(10**13,R,14)
    elif L<10**4:
        ans+=num(L,9999,4)
        ans+=ls[4]
        ans+=ls[5]
        ans+=ls[6]
        ans+=ls[7]
        ans+=ls[8]
        ans+=ls[9]
        ans+=ls[10]
        ans+=ls[11]
        ans+=ls[12]
        ans+=num(10**13,R,14)
    elif L<10**5:
        ans+=num(L,99999,5)
        ans+=ls[5]
        ans+=ls[6]
        ans+=ls[7]
        ans+=ls[8]
        ans+=ls[9]
        ans+=ls[10]
        ans+=ls[11]
        ans+=ls[12]
        ans+=num(10**13,R,14)
    elif L<10**6:
        ans+=num(L,10**6-1,6)
        ans+=ls[6]
        ans+=ls[7]
        ans+=ls[8]
        ans+=ls[9]
        ans+=ls[10]
        ans+=ls[11]
        ans+=ls[12]
        ans+=num(10**13,R,14)
    elif L<10**7:
        ans+=num(L,10**7-1,7)
        ans+=ls[7]
        ans+=ls[8]
        ans+=ls[9]
        ans+=ls[10]
        ans+=ls[11]
        ans+=ls[12]
        ans+=num(10**13,R,14)
    elif L<10**8:
        ans+=num(L,10**8-1,8)
        ans+=ls[8]
        ans+=ls[9]
        ans+=ls[10]
        ans+=ls[11]
        ans+=ls[12]
        ans+=num(10**13,R,14)
    elif L<10**9:
        ans+=num(L,10**9-1,9)
        ans+=ls[9]
        ans+=ls[10]
        ans+=ls[11]
        ans+=ls[12]
        ans+=num(10**13,R,14)
    elif L<10**10:
        ans+=num(L,10**10-1,10)
        ans+=ls[10]
        ans+=ls[11]
        ans+=ls[12]
        ans+=num(10**13,R,14)
    elif L<10**11:
        ans+=num(L,10**11-1,11)
        ans+=ls[11]
        ans+=ls[12]
        ans+=num(10**13,R,14)
    elif L<10**12:
        ans+=num(L,10**12-1,12)
        ans+=ls[12]
        ans+=num(10**13,R,14)
    elif L<10**13:
        ans+=num(L,10**13-1,13)
        ans+=num(10**13,R,14)
    else:
        ans+=num(L,R,14)
elif R < 10 ** 15:
    if L<10:
        ans+=num(L,9,1)
        ans+=ls[1]
        ans+=ls[2]
        ans+=ls[3]
        ans+=ls[4]
        ans+=ls[5]
        ans+=ls[6]
        ans+=ls[7]
        ans+=ls[8]
        ans+=ls[9]
        ans+=ls[10]
        ans+=ls[11]
        ans+=ls[12]
        ans+=ls[13]
        ans+=num(10**14,R,15)
    elif L<100:
        ans+=num(L,99,2)
        ans+=ls[2]
        ans+=ls[3]
        ans+=ls[4]
        ans+=ls[5]
        ans+=ls[6]
        ans+=ls[7]
        ans+=ls[8]
        ans+=ls[9]
        ans+=ls[10]
        ans+=ls[11]
        ans+=ls[12]
        ans+=ls[13]
        ans+=num(10**14,R,15)
    elif L<1000:
        ans+=num(L,999,3)
        ans+=ls[3]
        ans+=ls[4]
        ans+=ls[5]
        ans+=ls[6]
        ans+=ls[7]
        ans+=ls[8]
        ans+=ls[9]
        ans+=ls[10]
        ans+=ls[11]
        ans+=ls[12]
        ans+=ls[13]
        ans+=num(10**14,R,15)
    elif L<10**4:
        ans+=num(L,9999,4)
        ans+=ls[4]
        ans+=ls[5]
        ans+=ls[6]
        ans+=ls[7]
        ans+=ls[8]
        ans+=ls[9]
        ans+=ls[10]
        ans+=ls[11]
        ans+=ls[12]
        ans+=ls[13]
        ans+=num(10**14,R,15)
    elif L<10**5:
        ans+=num(L,99999,5)
        ans+=ls[5]
        ans+=ls[6]
        ans+=ls[7]
        ans+=ls[8]
        ans+=ls[9]
        ans+=ls[10]
        ans+=ls[11]
        ans+=ls[12]
        ans+=ls[13]
        ans+=num(10**14,R,15)
    elif L<10**6:
        ans+=num(L,10**6-1,6)
        ans+=ls[6]
        ans+=ls[7]
        ans+=ls[8]
        ans+=ls[9]
        ans+=ls[10]
        ans+=ls[11]
        ans+=ls[12]
        ans+=ls[13]
        ans+=num(10**14,R,15)
    elif L<10**7:
        ans+=num(L,10**7-1,7)
        ans+=ls[7]
        ans+=ls[8]
        ans+=ls[9]
        ans+=ls[10]
        ans+=ls[11]
        ans+=ls[12]
        ans+=ls[13]
        ans+=num(10**14,R,15)
    elif L<10**8:
        ans+=num(L,10**8-1,8)
        ans+=ls[8]
        ans+=ls[9]
        ans+=ls[10]
        ans+=ls[11]
        ans+=ls[12]
        ans+=ls[13]
        ans+=num(10**14,R,15)
    elif L<10**9:
        ans+=num(L,10**9-1,9)
        ans+=ls[9]
        ans+=ls[10]
        ans+=ls[11]
        ans+=ls[12]
        ans+=ls[13]
        ans+=num(10**14,R,15)
    elif L<10**10:
        ans+=num(L,10**10-1,10)
        ans+=ls[10]
        ans+=ls[11]
        ans+=ls[12]
        ans+=ls[13]
        ans+=num(10**14,R,15)
    elif L<10**11:
        ans+=num(L,10**11-1,11)
        ans+=ls[11]
        ans+=ls[12]
        ans+=ls[13]
        ans+=num(10**14,R,15)
    elif L<10**12:
        ans+=num(L,10**12-1,12)
        ans+=ls[12]
        ans+=ls[13]
        ans+=num(10**14,R,15)
    elif L<10**13:
        ans+=num(L,10**13-1,13)
        ans+=ls[13]
        ans+=num(10**14,R,15)
    elif L<10**14:
        ans+=num(L,10**14-1,14)
        ans+=num(10**14,R,15)
    else:
        ans+=num(L,R,15)
elif R < 10 ** 16:
    if L<10:
        ans+=num(L,9,1)
        ans+=ls[1]
        ans+=ls[2]
        ans+=ls[3]
        ans+=ls[4]
        ans+=ls[5]
        ans+=ls[6]
        ans+=ls[7]
        ans+=ls[8]
        ans+=ls[9]
        ans+=ls[10]
        ans+=ls[11]
        ans+=ls[12]
        ans+=ls[13]
        ans+=ls[14]
        ans+=num(10**15,R,16)
    elif L<100:
        ans+=num(L,99,2)
        ans+=ls[2]
        ans+=ls[3]
        ans+=ls[4]
        ans+=ls[5]
        ans+=ls[6]
        ans+=ls[7]
        ans+=ls[8]
        ans+=ls[9]
        ans+=ls[10]
        ans+=ls[11]
        ans+=ls[12]
        ans+=ls[13]
        ans+=ls[14]
        ans+=num(10**15,R,16)
    elif L<1000:
        ans+=num(L,999,3)
        ans+=ls[3]
        ans+=ls[4]
        ans+=ls[5]
        ans+=ls[6]
        ans+=ls[7]
        ans+=ls[8]
        ans+=ls[9]
        ans+=ls[10]
        ans+=ls[11]
        ans+=ls[12]
        ans+=ls[13]
        ans+=ls[14]
        ans+=num(10**15,R,16)
    elif L<10**4:
        ans+=num(L,9999,4)
        ans+=ls[4]
        ans+=ls[5]
        ans+=ls[6]
        ans+=ls[7]
        ans+=ls[8]
        ans+=ls[9]
        ans+=ls[10]
        ans+=ls[11]
        ans+=ls[12]
        ans+=ls[13]
        ans+=ls[14]
        ans+=num(10**15,R,16)
    elif L<10**5:
        ans+=num(L,99999,5)
        ans+=ls[5]
        ans+=ls[6]
        ans+=ls[7]
        ans+=ls[8]
        ans+=ls[9]
        ans+=ls[10]
        ans+=ls[11]
        ans+=ls[12]
        ans+=ls[13]
        ans+=ls[14]
        ans+=num(10**15,R,16)
    elif L<10**6:
        ans+=num(L,10**6-1,6)
        ans+=ls[6]
        ans+=ls[7]
        ans+=ls[8]
        ans+=ls[9]
        ans+=ls[10]
        ans+=ls[11]
        ans+=ls[12]
        ans+=ls[13]
        ans+=ls[14]
        ans+=num(10**15,R,16)
    elif L<10**7:
        ans+=num(L,10**7-1,7)
        ans+=ls[7]
        ans+=ls[8]
        ans+=ls[9]
        ans+=ls[10]
        ans+=ls[11]
        ans+=ls[12]
        ans+=ls[13]
        ans+=ls[14]
        ans+=num(10**15,R,16)
    elif L<10**8:
        ans+=num(L,10**8-1,8)
        ans+=ls[8]
        ans+=ls[9]
        ans+=ls[10]
        ans+=ls[11]
        ans+=ls[12]
        ans+=ls[13]
        ans+=ls[14]
        ans+=num(10**15,R,16)
    elif L<10**9:
        ans+=num(L,10**9-1,9)
        ans+=ls[9]
        ans+=ls[10]
        ans+=ls[11]
        ans+=ls[12]
        ans+=ls[13]
        ans+=ls[14]
        ans+=num(10**15,R,16)
    elif L<10**10:
        ans+=num(L,10**10-1,10)
        ans+=ls[10]
        ans+=ls[11]
        ans+=ls[12]
        ans+=ls[13]
        ans+=ls[14]
        ans+=num(10**15,R,16)
    elif L<10**11:
        ans+=num(L,10**11-1,11)
        ans+=ls[11]
        ans+=ls[12]
        ans+=ls[13]
        ans+=ls[14]
        ans+=num(10**15,R,16)
    elif L<10**12:
        ans+=num(L,10**12-1,12)
        ans+=ls[12]
        ans+=ls[13]
        ans+=ls[14]
        ans+=num(10**15,R,16)
    elif L<10**13:
        ans+=num(L,10**13-1,13)
        ans+=ls[13]
        ans+=ls[14]
        ans+=num(10**15,R,16)
    elif L<10**14:
        ans+=num(L,10**14-1,14)
        ans+=ls[14]
        ans+=num(10**15,R,16)
    elif L<10**15:
        ans+=num(L,10**15-1,15)
        ans+=num(10**15,R,16)
    else:
        ans+=num(L,R,16)
elif R < 10 ** 17:
    if L<10:
        ans+=num(L,9,1)
        ans+=ls[1]
        ans+=ls[2]
        ans+=ls[3]
        ans+=ls[4]
        ans+=ls[5]
        ans+=ls[6]
        ans+=ls[7]
        ans+=ls[8]
        ans+=ls[9]
        ans+=ls[10]
        ans+=ls[11]
        ans+=ls[12]
        ans+=ls[13]
        ans+=ls[14]
        ans+=ls[15]
        ans+=num(10**16,R,17)
    elif L<100:
        ans+=num(L,99,2)
        ans+=ls[2]
        ans+=ls[3]
        ans+=ls[4]
        ans+=ls[5]
        ans+=ls[6]
        ans+=ls[7]
        ans+=ls[8]
        ans+=ls[9]
        ans+=ls[10]
        ans+=ls[11]
        ans+=ls[12]
        ans+=ls[13]
        ans+=ls[14]
        ans+=ls[15]
        ans+=num(10**16,R,17)
    elif L<1000:
        ans+=num(L,999,3)
        ans+=ls[3]
        ans+=ls[4]
        ans+=ls[5]
        ans+=ls[6]
        ans+=ls[7]
        ans+=ls[8]
        ans+=ls[9]
        ans+=ls[10]
        ans+=ls[11]
        ans+=ls[12]
        ans+=ls[13]
        ans+=ls[14]
        ans+=ls[15]
        ans+=num(10**16,R,17)
    elif L<10**4:
        ans+=num(L,9999,4)
        ans+=ls[4]
        ans+=ls[5]
        ans+=ls[6]
        ans+=ls[7]
        ans+=ls[8]
        ans+=ls[9]
        ans+=ls[10]
        ans+=ls[11]
        ans+=ls[12]
        ans+=ls[13]
        ans+=ls[14]
        ans+=ls[15]
        ans+=num(10**16,R,17)
    elif L<10**5:
        ans+=num(L,99999,5)
        ans+=ls[5]
        ans+=ls[6]
        ans+=ls[7]
        ans+=ls[8]
        ans+=ls[9]
        ans+=ls[10]
        ans+=ls[11]
        ans+=ls[12]
        ans+=ls[13]
        ans+=ls[14]
        ans+=ls[15]
        ans+=num(10**16,R,17)
    elif L<10**6:
        ans+=num(L,10**6-1,6)
        ans+=ls[6]
        ans+=ls[7]
        ans+=ls[8]
        ans+=ls[9]
        ans+=ls[10]
        ans+=ls[11]
        ans+=ls[12]
        ans+=ls[13]
        ans+=ls[14]
        ans+=ls[15]
        ans+=num(10**16,R,17)
    elif L<10**7:
        ans+=num(L,10**7-1,7)
        ans+=ls[7]
        ans+=ls[8]
        ans+=ls[9]
        ans+=ls[10]
        ans+=ls[11]
        ans+=ls[12]
        ans+=ls[13]
        ans+=ls[14]
        ans+=ls[15]
        ans+=num(10**16,R,17)
    elif L<10**8:
        ans+=num(L,10**8-1,8)
        ans+=ls[8]
        ans+=ls[9]
        ans+=ls[10]
        ans+=ls[11]
        ans+=ls[12]
        ans+=ls[13]
        ans+=ls[14]
        ans+=ls[15]
        ans+=num(10**16,R,17)
    elif L<10**9:
        ans+=num(L,10**9-1,9)
        ans+=ls[9]
        ans+=ls[10]
        ans+=ls[11]
        ans+=ls[12]
        ans+=ls[13]
        ans+=ls[14]
        ans+=ls[15]
        ans+=num(10**16,R,17)
    elif L<10**10:
        ans+=num(L,10**10-1,10)
        ans+=ls[10]
        ans+=ls[11]
        ans+=ls[12]
        ans+=ls[13]
        ans+=ls[14]
        ans+=ls[15]
        ans+=num(10**16,R,17)
    elif L<10**11:
        ans+=num(L,10**11-1,11)
        ans+=ls[11]
        ans+=ls[12]
        ans+=ls[13]
        ans+=ls[14]
        ans+=ls[15]
        ans+=num(10**16,R,17)
    elif L<10**12:
        ans+=num(L,10**12-1,12)
        ans+=ls[12]
        ans+=ls[13]
        ans+=ls[14]
        ans+=ls[15]
        ans+=num(10**16,R,17)
    elif L<10**13:
        ans+=num(L,10**13-1,13)
        ans+=ls[13]
        ans+=ls[14]
        ans+=ls[15]
        ans+=num(10**16,R,17)
    elif L<10**14:
        ans+=num(L,10**14-1,14)
        ans+=ls[14]
        ans+=ls[15]
        ans+=num(10**16,R,17)
    elif L<10**15:
        ans+=num(L,10**15-1,15)
        ans+=ls[15]
        ans+=num(10**16,R,17)
    elif L<10**16:
        ans+=num(L,10**16-1,16)
        ans+=num(10**16,R,17)
    else:
        ans+=num(L,R,17)
elif R < 10 ** 18:
    if L<10:
        ans+=num(L,9,1)
        ans+=ls[1]
        ans+=ls[2]
        ans+=ls[3]
        ans+=ls[4]
        ans+=ls[5]
        ans+=ls[6]
        ans+=ls[7]
        ans+=ls[8]
        ans+=ls[9]
        ans+=ls[10]
        ans+=ls[11]
        ans+=ls[12]
        ans+=ls[13]
        ans+=ls[14]
        ans+=ls[15]
        ans+=ls[16]
        ans+=num(10**17,R,18)
    elif L<100:
        ans+=num(L,99,2)
        ans+=ls[2]
        ans+=ls[3]
        ans+=ls[4]
        ans+=ls[5]
        ans+=ls[6]
        ans+=ls[7]
        ans+=ls[8]
        ans+=ls[9]
        ans+=ls[10]
        ans+=ls[11]
        ans+=ls[12]
        ans+=ls[13]
        ans+=ls[14]
        ans+=ls[15]
        ans+=ls[16]
        ans+=num(10**17,R,18)
    elif L<1000:
        ans+=num(L,999,3)
        ans+=ls[3]
        ans+=ls[4]
        ans+=ls[5]
        ans+=ls[6]
        ans+=ls[7]
        ans+=ls[8]
        ans+=ls[9]
        ans+=ls[10]
        ans+=ls[11]
        ans+=ls[12]
        ans+=ls[13]
        ans+=ls[14]
        ans+=ls[15]
        ans+=ls[16]
        ans+=num(10**17,R,18)
    elif L<10**4:
        ans+=num(L,9999,4)
        ans+=ls[4]
        ans+=ls[5]
        ans+=ls[6]
        ans+=ls[7]
        ans+=ls[8]
        ans+=ls[9]
        ans+=ls[10]
        ans+=ls[11]
        ans+=ls[12]
        ans+=ls[13]
        ans+=ls[14]
        ans+=ls[15]
        ans+=ls[16]
        ans+=num(10**17,R,18)
    elif L<10**5:
        ans+=num(L,99999,5)
        ans+=ls[5]
        ans+=ls[6]
        ans+=ls[7]
        ans+=ls[8]
        ans+=ls[9]
        ans+=ls[10]
        ans+=ls[11]
        ans+=ls[12]
        ans+=ls[13]
        ans+=ls[14]
        ans+=ls[15]
        ans+=ls[16]
        ans+=num(10**17,R,18)
    elif L<10**6:
        ans+=num(L,10**6-1,6)
        ans+=ls[6]
        ans+=ls[7]
        ans+=ls[8]
        ans+=ls[9]
        ans+=ls[10]
        ans+=ls[11]
        ans+=ls[12]
        ans+=ls[13]
        ans+=ls[14]
        ans+=ls[15]
        ans+=ls[16]
        ans+=num(10**17,R,18)
    elif L<10**7:
        ans+=num(L,10**7-1,7)
        ans+=ls[7]
        ans+=ls[8]
        ans+=ls[9]
        ans+=ls[10]
        ans+=ls[11]
        ans+=ls[12]
        ans+=ls[13]
        ans+=ls[14]
        ans+=ls[15]
        ans+=ls[16]
        ans+=num(10**17,R,18)
    elif L<10**8:
        ans+=num(L,10**8-1,8)
        ans+=ls[8]
        ans+=ls[9]
        ans+=ls[10]
        ans+=ls[11]
        ans+=ls[12]
        ans+=ls[13]
        ans+=ls[14]
        ans+=ls[15]
        ans+=ls[16]
        ans+=num(10**17,R,18)
    elif L<10**9:
        ans+=num(L,10**9-1,9)
        ans+=ls[9]
        ans+=ls[10]
        ans+=ls[11]
        ans+=ls[12]
        ans+=ls[13]
        ans+=ls[14]
        ans+=ls[15]
        ans+=ls[16]
        ans+=num(10**17,R,18)
    elif L<10**10:
        ans+=num(L,10**10-1,10)
        ans+=ls[10]
        ans+=ls[11]
        ans+=ls[12]
        ans+=ls[13]
        ans+=ls[14]
        ans+=ls[15]
        ans+=ls[16]
        ans+=num(10**17,R,18)
    elif L<10**11:
        ans+=num(L,10**11-1,11)
        ans+=ls[11]
        ans+=ls[12]
        ans+=ls[13]
        ans+=ls[14]
        ans+=ls[15]
        ans+=ls[16]
        ans+=num(10**17,R,18)
    elif L<10**12:
        ans+=num(L,10**12-1,12)
        ans+=ls[12]
        ans+=ls[13]
        ans+=ls[14]
        ans+=ls[15]
        ans+=ls[16]
        ans+=num(10**17,R,18)
    elif L<10**13:
        ans+=num(L,10**13-1,13)
        ans+=ls[13]
        ans+=ls[14]
        ans+=ls[15]
        ans+=ls[16]
        ans+=num(10**17,R,18)
    elif L<10**14:
        ans+=num(L,10**14-1,14)
        ans+=ls[14]
        ans+=ls[15]
        ans+=ls[16]
        ans+=num(10**17,R,18)
    elif L<10**15:
        ans+=num(L,10**15-1,15)
        ans+=ls[15]
        ans+=ls[16]
        ans+=num(10**17,R,18)
    elif L<10**16:
        ans+=num(L,10**16-1,16)
        ans+=ls[16]
        ans+=num(10**17,R,18)
    elif L<10**17:
        ans+=num(L,10**17-1,17)
        ans+=num(10**17,R,18)
    else:
        ans+=num(L,R,18)
else:
    #Ex = num(10**18,10**18,19)
    Ex = 19000000000000000000
    if L<10:
        ans+=num(L,9,1)
        ans+=ls[1]
        ans+=ls[2]
        ans+=ls[3]
        ans+=ls[4]
        ans+=ls[5]
        ans+=ls[6]
        ans+=ls[7]
        ans+=ls[8]
        ans+=ls[9]
        ans+=ls[10]
        ans+=ls[11]
        ans+=ls[12]
        ans+=ls[13]
        ans+=ls[14]
        ans+=ls[15]
        ans+=ls[16]
        ans+=ls[17]
        ans+=Ex
    elif L<100:
        ans+=num(L,99,2)
        ans+=ls[2]
        ans+=ls[3]
        ans+=ls[4]
        ans+=ls[5]
        ans+=ls[6]
        ans+=ls[7]
        ans+=ls[8]
        ans+=ls[9]
        ans+=ls[10]
        ans+=ls[11]
        ans+=ls[12]
        ans+=ls[13]
        ans+=ls[14]
        ans+=ls[15]
        ans+=ls[16]
        ans+=ls[17]
        ans+=Ex
    elif L<1000:
        ans+=num(L,999,3)
        ans+=ls[3]
        ans+=ls[4]
        ans+=ls[5]
        ans+=ls[6]
        ans+=ls[7]
        ans+=ls[8]
        ans+=ls[9]
        ans+=ls[10]
        ans+=ls[11]
        ans+=ls[12]
        ans+=ls[13]
        ans+=ls[14]
        ans+=ls[15]
        ans+=ls[16]
        ans+=ls[17]
        ans+=Ex
    elif L<10**4:
        ans+=num(L,9999,4)
        ans+=ls[4]
        ans+=ls[5]
        ans+=ls[6]
        ans+=ls[7]
        ans+=ls[8]
        ans+=ls[9]
        ans+=ls[10]
        ans+=ls[11]
        ans+=ls[12]
        ans+=ls[13]
        ans+=ls[14]
        ans+=ls[15]
        ans+=ls[16]
        ans+=ls[17]
        ans+=Ex
    elif L<10**5:
        ans+=num(L,99999,5)
        ans+=ls[5]
        ans+=ls[6]
        ans+=ls[7]
        ans+=ls[8]
        ans+=ls[9]
        ans+=ls[10]
        ans+=ls[11]
        ans+=ls[12]
        ans+=ls[13]
        ans+=ls[14]
        ans+=ls[15]
        ans+=ls[16]
        ans+=ls[17]
        ans+=Ex
    elif L<10**6:
        ans+=num(L,10**6-1,6)
        ans+=ls[6]
        ans+=ls[7]
        ans+=ls[8]
        ans+=ls[9]
        ans+=ls[10]
        ans+=ls[11]
        ans+=ls[12]
        ans+=ls[13]
        ans+=ls[14]
        ans+=ls[15]
        ans+=ls[16]
        ans+=ls[17]
        ans+=Ex
    elif L<10**7:
        ans+=num(L,10**7-1,7)
        ans+=ls[7]
        ans+=ls[8]
        ans+=ls[9]
        ans+=ls[10]
        ans+=ls[11]
        ans+=ls[12]
        ans+=ls[13]
        ans+=ls[14]
        ans+=ls[15]
        ans+=ls[16]
        ans+=ls[17]
        ans+=Ex
    elif L<10**8:
        ans+=num(L,10**8-1,8)
        ans+=ls[8]
        ans+=ls[9]
        ans+=ls[10]
        ans+=ls[11]
        ans+=ls[12]
        ans+=ls[13]
        ans+=ls[14]
        ans+=ls[15]
        ans+=ls[16]
        ans+=ls[17]
        ans+=Ex
    elif L<10**9:
        ans+=num(L,10**9-1,9)
        ans+=ls[9]
        ans+=ls[10]
        ans+=ls[11]
        ans+=ls[12]
        ans+=ls[13]
        ans+=ls[14]
        ans+=ls[15]
        ans+=ls[16]
        ans+=ls[17]
        ans+=Ex
    elif L<10**10:
        ans+=num(L,10**10-1,10)
        ans+=ls[10]
        ans+=ls[11]
        ans+=ls[12]
        ans+=ls[13]
        ans+=ls[14]
        ans+=ls[15]
        ans+=ls[16]
        ans+=ls[17]
        ans+=Ex
    elif L<10**11:
        ans+=num(L,10**11-1,11)
        ans+=ls[11]
        ans+=ls[12]
        ans+=ls[13]
        ans+=ls[14]
        ans+=ls[15]
        ans+=ls[16]
        ans+=ls[17]
        ans+=Ex
    elif L<10**12:
        ans+=num(L,10**12-1,12)
        ans+=ls[12]
        ans+=ls[13]
        ans+=ls[14]
        ans+=ls[15]
        ans+=ls[16]
        ans+=ls[17]
        ans+=Ex
    elif L<10**13:
        ans+=num(L,10**13-1,13)
        ans+=ls[13]
        ans+=ls[14]
        ans+=ls[15]
        ans+=ls[16]
        ans+=ls[17]
        ans+=Ex
    elif L<10**14:
        ans+=num(L,10**14-1,14)
        ans+=ls[14]
        ans+=ls[15]
        ans+=ls[16]
        ans+=ls[17]
        ans+=Ex
    elif L<10**15:
        ans+=num(L,10**15-1,15)
        ans+=ls[15]
        ans+=ls[16]
        ans+=ls[17]
        ans+=Ex
    elif L<10**16:
        ans+=num(L,10**16-1,16)
        ans+=ls[16]
        ans+=ls[17]
        ans+=Ex
    elif L<10**17:
        ans+=num(L,10**17-1,17)
        ans+=ls[17]
        ans+=Ex
    elif L<10**18:
        ans+=num(L,10**18-1,18)
        ans+=Ex
    else:
        ans+=Ex
mod = 10 ** 9 + 7
print(ans%mod)

