from collections import defaultdict

def canFinish(numCourses, prerequisites):

    a = set([v[0] for v in prerequisites])
    b = set([v[1] for v in prerequisites])
    courses = a.difference(b)

    map_prereq = {}
    for prereq in prerequisites:
        if prereq[1] in map_prereq:
            map_prereq[prereq[1]].add(prereq[0])
        else:
            map_prereq[prereq[1]] = set()
            map_prereq[prereq[1]].add(prereq[0])


    i = 0
    while i < len(map_prereq):
        key = list(map_prereq.keys())[i]
        if map_prereq[key].issubset(courses):
            courses.add(key)
            map_prereq.pop(key)
            i = -1

        i += 1
    if not map_prereq:
        return True

    return numCourses <= len(courses)


def canFinish(numCourses, prerequisites):
    
    adj_list = defaultdict(lambda: [])
    in_degrees = defaultdict(lambda: 0)
    
    for course, prereq in prerequisites:
        adj_list[prereq].append(course)
        in_degrees[course] += 1
        
    # Get the ready nodes
    ready = []
    for i in range(0, numCourses):
        if in_degrees[i] == 0:
            ready.append(i)
            
    # Kahn's algorithm
    ordering = []
    while ready:
        curr_course = ready.pop()
        ordering.append(curr_course)
        for course in adj_list[curr_course]:
            in_degrees[course] -= 1
            if in_degrees[course] == 0:
                ready.append(course)
    
    return len(ordering) == numCourses

# canFinish(numCourses = 5, prerequisites = [])
canFinish(numCourses = 5, prerequisites = [[1,4],[2,4],[3,1],[3,2]])
canFinish(numCourses = 3, prerequisites = [[1,0], [0,2], [1,2]])
canFinish(numCourses = 2, prerequisites = [[1,0]])
canFinish(numCourses = 2, prerequisites = [[1,0],[0,1]])