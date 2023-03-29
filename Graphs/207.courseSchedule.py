# DFS recursive

def canFinish(numCourses, prerequisites):
    # Map each courses to prereq list
    preMap = { i: [] for i in range(numCourses)}
    for crs, pre in prerequisites:
        preMap[crs].append(pre)
    # return preMap  {1: [0], 1: [0]}
    
    visited = set()
    def dfs(crs):
        if crs in visited:
            return False
        if preMap[crs] == []:
            return True
        
        visited.add(crs)
        for pre in preMap[crs]:
            if not dfs(pre): 
                return False
        visited.remove(crs)
        preMap[crs] = []
        return True
    
    for crs in range(numCourses):
        if not dfs(crs):
            return False
    return True


print(canFinish(2, [[1, 0]])) # true
print(canFinish(2, [[1, 0], [0, 1]])) # false
