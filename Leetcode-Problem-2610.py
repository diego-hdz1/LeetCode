class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        myMap = {}  
        solution = []
        for num in nums:
            if num in myMap:
                myMap[num] += 1
            else:
                myMap[num] = 1
        
        while myMap:
            temp = []
            for key in list(myMap):
                if myMap[key] == 0:
                    del myMap[key]
                else:
                    temp.append(key)
                    myMap[key] -= 1
            if myMap:
                solution.append(temp)
      
        return solution