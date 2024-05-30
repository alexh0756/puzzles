from collections import defaultdict


def findOrder(numCourses, prerequisites):

    courses = defaultdict(lambda: [])
    prereqs = defaultdict(lambda: 0)

    for course, prereq in prerequisites:
        courses[prereq].append(course)
        prereqs[course] += 1

    order = []
    for i in range(numCourses):
        if prereqs[i] == 0:
            order.append(i)

    i = 0
    while i < len(order):
        course = order[i]
        next_courses = courses[course]
        for next in next_courses:
            prereqs[next] -= 1
            if prereqs[next] == 0:
                order.append(next)
        i += 1

    return order if len(order) >= numCourses else []

print(findOrder(numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]))
print(findOrder(numCourses = 2, prerequisites = [[1,0]]))