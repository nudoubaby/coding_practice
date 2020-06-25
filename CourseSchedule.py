# 207. Course Schedule
# https://leetcode.com/problems/course-schedule/

def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    #graph is represented by edge lists without edge weights
    #[,prerequisties], converting it to a adjacency list
    d = collections.defaultdict(list)
    level = numCourses*[0]
    for a, b in prerequisites:
        d[a].append(b)
        level[b] += 1
    # if level[i]>0, course i is a prerequisite of other courses
    visited = [i for i in range(numCourses) if level[i]==0]
    # print('1',visited)
    while visited:
        # print('2',visited)
        temp =[]
        for i in visited:
            level[i] -= 1
            for j in d[i]:
                level[j] -= 1
                if level[j] == 0:
                    temp.append(j)
        if temp: 
            visited = temp
        elif max(level) <0:
            return True
        else:
            return False
    return False   
