__author__ = 'jaundice'
#动态规划，最长公共子序列
def alc():
    #str1='ABCDGH'
    #str2='AEDFHR'
    str1='AGGTAB'
    str2='GXTXAYB'
    ss= [([0] * len(str2)) for i in range(len(str1))]
    for i in range(len(str1)):
        for j in range(len(str2)):
            if i==0 and j==0:
                if str1[i]==str2[j]:
                    ss[i][j]=1
                else:
                    ss[i][j]=0
            else:
                if str1[i]==str2[j]:
                    if i-1>=0 and j-1>=0:
                        ss[i][j]=ss[i-1][j-1]+1
                    elif i-1>=0 and j-1 <0:
                        ss[i][j]=1
                    elif i-1<0 and j-1>=0:
                        ss[i][j]=1
                else:
                    if i-1>=0 and j-1>=0:
                        ss[i][j]=max(ss[i-1][j],ss[i][j-1])
                    elif i-1>=0 and j-1 <0:
                        ss[i][j]=max(ss[i-1][j],ss[i][0])
                    elif i-1<0 and j-1>=0:
                        ss[i][j]=max(ss[0][j],ss[i][j-1])

    print ss

alc()



