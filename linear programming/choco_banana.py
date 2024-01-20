import numpy as np

array = np.zeros([7, 7])

array[1, :] = 1
array[4, :] = 1
array[:, 3] = 1
array[2, 2:5] = 1
array[3, 3] = 0
array[3, 4] = 1

constraints = {(0, 1): 6,
              (1, 7): 3,
              (2, 3): 3,
              (3, 2): 6,
              (3, 3): 1,
              (4, 3): 4,
              (3, 4): 5,
              (5, 0): 5,
              (6, 5): 4,
              }

solution = np.array([[1., 0., 0., 1., 1., 0., 0.,],
                    [1., 0., 1., 0., 0., 1., 0.,],
                    [1., 0., 1., 0., 1., 0., 1.,],
                    [1., 0., 0., 1., 0., 0., 1.,],
                    [0., 1., 1., 0., 1., 0., 0.,],
                    [0., 1., 1., 0., 0., 1., 1.,],
                    [0., 0., 0., 1., 0., 1., 1.,]])

array = solution

def check_surroundings(input):
    lst = []
    for i, j in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        coord = (input[0]+i, input[1]+j)
        if (-1 in coord) or (7 in coord):
            continue
        lst.append(coord)
    return lst

def is_rectangle(lst):
    lst = lst[1:]

    lst.sort(key=sum)

    x_dist = lst[-1][0] - lst[0][0]
    y_dist = lst[-1][1] - lst[0][1]

    if len(lst) != ((x_dist + 1) * (y_dist + 1)):
        print("not a rectange")
        return False
    
    for x in range(x_dist):
        for y in range(y_dist):
            if (lst[0][0] + x, lst[0][1] + y) not in lst:
                # print("not a rectange")
                return False

    # print("is a rectangle")
    return True

def check_constraint(constraints, groups):

    for k, v in constraints.items():
        for group_k, group_v in groups.items():
            if k in group_v[1:]:
                if v != len(group_v)-1:
                    print(f"group {group_k} violated assumption {v}")

    return
    

remaining = []
for i in range(7):
    for j in range(7):
        remaining.append((i, j))
remaining.sort(key=sum)

groups = {}
coord = remaining[0]
key = 0
type = array[coord]
groups.update({key: [type, coord]})
remaining.pop(remaining.index(coord))
next = []

while len(remaining) > 0:
    for i in check_surroundings(coord):
        if (array[i] == type) and (i in remaining):
            remaining.pop(remaining.index(i))
            next.append(i)
            groups[key].append(i)

    if len(next) > 0:
        coord = next[0]
        next.pop(0)
    else:
        coord = remaining[0]
        remaining.pop(remaining.index(coord))
        next = []

        type = array[coord]
        key += 1
        groups.update({key: [type, coord]})

for k, v in groups.items():
    cond1 = ((v[0] == 0) and not is_rectangle(v))
    cond2 = ((v[0] == 1) and is_rectangle(v))

    if cond1 or cond2:
        print('passed')
    else:
        print('failed')

check_constraint(constraints, groups)

print('finished')
    

