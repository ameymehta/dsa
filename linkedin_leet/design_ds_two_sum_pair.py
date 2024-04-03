class TwoSum(object):

    def __init__(self):
        self.nums = []
        self.nums_map = {}

    def add(self, number):
        """
        :type number: int
        :rtype: None
        """
        self.nums.append(number)
        if number not in self.nums_map:
            self.nums_map[number] = 0
        self.nums_map[number] += 1

    def find(self, value):
        """
        :type value: int
        :rtype: bool
        """
        for num in self.nums:
            pair = value - num
            if pair == num and self.nums_map[num] > 1:
                return True
            if pair != num and pair in self.nums_map:
                return True
        return False
        
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)