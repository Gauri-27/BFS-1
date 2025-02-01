# Time Complexity : O(V + E)
# Space Compexity : O(V+E)
from collections import deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if  numCourses == 0:
            return True
        indegree = [0]*numCourses
        dependency = {i : [] for i in range(numCourses)}
        

        for course, pre in prerequisites:
            dependency[pre].append(course)
            indegree[course] = 1 + indegree[course]

        completed_courses = 0
        queue = deque(i for i in range(numCourses) if indegree[i] ==0)
        while queue:
            course = queue.popleft()
            completed_courses += 1

            for next_course in dependency[course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)
        return completed_courses == numCourses