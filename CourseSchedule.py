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

# 210. Course Schedule II
def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    # courses whose prerequisites is lesest
    # chourse which is not a prerequirsite of others
    d = collections.defaultdict(list)
    level = numCourses*[0]
    for a, b in prerequisites: #b is a's prerequisiste
        d[b].append(a)
        level[a] += 1
    res = []
    curr = [i for i in range(numCourses) if level[i]==0]
    while curr:
        temp = []
        for i in curr:
            level[i] -= 1
            res.append(i)
            for j in d[i]: 
                level[j] -= 1
                if level[j]== 0: 
                    temp.append(j) 
                    #print(temp)
        if temp != []: curr = temp
        #3 [[1,0],[1,2],[0,1]], second condition to avoid error: [2,2,1,0]
        elif max(level)<0 and len(res)==numCourses:
            return res
        #3 [[1,0],[1,2],[0,1]], error: time limited exceed
        else:
            return []
    return []
