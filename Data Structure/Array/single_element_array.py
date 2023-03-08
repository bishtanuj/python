class Solution:
    def findSingle(self, N, array):
        dictionary = {}
        for i in array:
            keys = dictionary.keys()
            if i in keys:
                dictionary[i] += 1
            else:
                dictionary[i] = 1
        keys = [key for key, value in dictionary.items() if value == 1]
        for i in range(len(keys)):
            return keys
    
if __name__ =='__main__':
    N = int(input("Enter the total number of array: "))
    array = input("Enter the elements: ").split()[:N]
    obj = Solution()
    print(f"Single element(s) in array: {obj.findSingle(N, array)}")
