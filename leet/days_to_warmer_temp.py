"""
https://leetcode.com/problems/daily-temperatures/description/?envType=study-plan-v2&envId=leetcode-75

Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
"""

from collections import deque

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        # q is being used as a stack. 
        # new additions from left and removals from left.
        q = deque()
        result = [0] * len(temperatures)

        # looping in reverse
        # [73,74,75,71,69,72,76,73]
        for i in range(len(temperatures) - 1, -1, -1):
            # this will be the case at the start. 
            # add to queue. no more days... so 0 for the result
            if not q:
                q.appendleft(i)
                result[i] = 0
            else:
                # take out all the colder days that are in q
                while q and temperatures[i] >= temperatures[q[0]]:
                    q.popleft()
                # if q is empty, add 0 to result for 
                # no definte number of days to warmer weather
                if not q:
                    result[i] = 0
                # if it is not empty, 
                # at to front of the queue is day warmer than i(th) day
                else:
                    result[i] = q[0] - i
                # add current day to the front of the queue (left of queue)
                q.appendleft(i)
        
        return result
    
    def dailyTemperatures_usingStack(self, temperatures):
        result = [0] * len(temperatures)
        stack = []

        # looping in reverse
        # [73,74,75,71,69,72,76,73]
        for i in range(len(temperatures) - 1, -1, -1):
            curr_temperature = temperatures[i]
            # take out all the colder days
            while stack and curr_temperature >= temperatures[stack[-1]]:
                stack.pop()

            # warmer day is at the top of the stack
            if stack:
                result[i] = stack[-1] - i

            # add current day to the stack
            stack.append(i)

        return result