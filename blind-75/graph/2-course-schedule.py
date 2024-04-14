class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = [[] for i in range(numCourses)]
        visit = [0 for i in range(numCourses)]
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        for course in range(numCourses):
            if not self.dfs(course, graph, visit):
                return False

        return True

    def dfs(self, course, graph, visit):
        # -1 means course is being visited, cycle/loop caguht
        if visit[course] == -1:
            return False
        # all prereqs of this course have been checked and visit was complete
        if visit[course] == 1:
            return True
        # mark the course -1 for on-going visit
        visit[course] = -1
        # traverse through each prereq/child of that course
        for prereq in graph[course]:
            if not self.dfs(prereq, graph, visit):
                return False
        # mark the course 1 for visit complete with no cycle
        # it will come to this line, only if no prereqs returned False
        visit[course] = 1
        return True
