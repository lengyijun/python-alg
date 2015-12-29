# -*- coding: utf-8 -*-
__author__ = 'jaundice'

def calc_lc(ss_list):
   dict={}
   for i in range(len(ss_list)):
      for j in range(i,len(ss_list)):
         sum=0
         for k in range(i,j+1):
            sum+=len(ss_list[k])
         sum+=j-i
         if sum>max_in_a_line:
            dict[(i,j)]=float("inf")
         elif sum<=max_in_a_line and j==len(ss_list)-1:
            dict[(i,j)]=0
         else:
            dict[(i,j)]=(-sum+max_in_a_line)**3
   return dict



if __name__ == '__main__':
   ss_list=["he","was","ok","where","which"]
   max_in_a_line=10

   lc=calc_lc(ss_list)
   result=[float("inf")] * (len(ss_list))
   result[0]=lc[(0,0)]
   for i in range(0,len(result)):
      if result[i]>lc[(0,i)]:
         result[i]=lc[(0,i)]
      for j in range(0,i):
         temp=result[j]+lc[(j+1,i)]
         if result[i]>temp:
            result[i]=temp
   print(result)
