#!/usr/bin/env python
# coding: utf-8

# # Programming problem 1

# In[22]:


def twoSum(nums, target):
        lst=[]
        for x in range(len(nums)):
            for y in range(x+1,len(nums)):
                if nums[x]+nums[y]==target:
                    lst.extend([x,y])
                    
        lst=list(set(lst))
        return lst

print(twoSum([2,7,11,15],9))
print(twoSum([3,2,4],6))
print(twoSum([3,3],6))


# # Programming problem 2

# In[41]:


lis=[]
for _ in range(int(input("Enter The Size: "))):
    name = input()
    score = float(input())
        
    lis.append([name,score])
    
lis.sort(key=lambda lis:lis[1])
    
second_lowest=[]
for i in range(len(lis)):
    if lis[i][1]!=lis[0][1]:
        second_lowest.append(lis[i][0])
        for j in range(i+1,len(lis)):
            if lis[j][1]==lis[i][1]:
                second_lowest.append(lis[j][0])
            else:
                break
        break        
           
                   
            
    else:
        continue
           

second_lowest.sort()
print("\nOutput: ")
for i in second_lowest:
    print(i)


# In[ ]:




