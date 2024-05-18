import numpy as np
import matplotlib.pyplot as plt
from quadtree import Point, Rect, QuadTree
from matplotlib import gridspec


width, height = 20, 20

DPI = 71
# np.random.seed(60)
# N = 500
# coords = np.random.randn(N, 2) * height/3 + (width/2, height/2)

coords = [
    [2, 5], [4, 6], [8, 5], [4, 0], [1, 1], 
    [19, 19], [1, 18], [16, 16], [12, 3], [7, 11],
    [14, 11], [9, 1], [1, 9], [10, 10], [1, 20], [20, 1]
    ]

points = [Point(*coord) for coord in coords]

domain = Rect(width/2, height/2, width, height)
qtree = QuadTree(domain, 3)
for point in points:
    qtree.insert(point)

print('Number of points in the domain =', len(qtree))

fig = plt.figure(figsize=(700/DPI, 500/DPI), dpi=DPI)
# fig = plt.figure()
ax = plt.subplot()
ax.set_xlim(0, width)
ax.set_ylim(0, height)
qtree.draw(ax)

ax.scatter([p.x for p in points], [p.y for p in points], s=4)
ax.set_xticks([])
ax.set_yticks([])

# region = Rect(5, 5, 10, 10)
# found_points = []
# qtree.query(region, found_points)
# print('Number of found points =', len(found_points))

# ax.scatter([p.x for p in found_points], [p.y for p in found_points],
#            facecolors='none', edgecolors='r', s=32)

# region.draw(ax, c='r')

ax.invert_yaxis()
plt.tight_layout()
plt.savefig('search-quadtree.png', DPI=72)
plt.show()
