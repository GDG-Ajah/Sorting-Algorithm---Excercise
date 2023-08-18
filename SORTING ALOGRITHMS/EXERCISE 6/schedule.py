# Course Schedule

# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

 

# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.
# Example 2:

# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 

# Constraints:

# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= 5000
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# All the pairs prerequisites[i] are unique.


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        # create a graph
        graph = [[] for _ in range(numCourses)]
        # create a visited array
        visited = [0 for _ in range(numCourses)]
        # create a stack
        stack = []
        # create a result array
        result = []
        # create a loop to add the edges to the graph
        for edge in prerequisites:
            graph[edge[0]].append(edge[1])
        # create a loop to traverse the graph
        for i in range(numCourses):
            if not self.dfs(graph, visited, stack, i):
                return False
        return True
    
    def dfs(self, graph, visited, stack, i):
        # check if the node is visited
        if visited[i] == -1:
            return False
        # check if the node is in the stack
        if visited[i] == 1:
            return True
        # mark the node as visited
        visited[i] = -1
        # create a loop to traverse the graph
        for j in graph[i]:
            if not self.dfs(graph, visited, stack, j):
                return False
        # mark the node as visited
        visited[i] = 1
        # add the node to the stack
        stack.append(i)
        return True