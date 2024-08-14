"""
#PROBLEM 1
Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
#1
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
#2
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
"""
lst1=list(map(int, input().split())) 
target_num1 = eval(input())

def twoSum(lst,target_num):
    for num1 in range(len(lst)):
        for num2 in range(num1+1,len(lst)):
            if(lst[num1]+lst[num2]==target_num):
                return (num1,num2)
                
print(list(twoSum(lst1,target_num1)))


#PROBLEM 2 Seprate even and odd numbers from list
lst=list(map(int, input().split()))
def evenOddEval(lst_of_num):
    new_lst=[]
    new_lst2=[]
    for i in lst_of_num:
        if i%2==0:
            new_lst.append(i)
        else:
            new_lst2.append(i)
    print('Even Num List:{}   Odd Num List:{}'.format(new_lst,new_lst2))
evenOddEval(lst)
