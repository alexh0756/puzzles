import heapq

class MedianFinder:

    def __init__(self):
        self.median = []
        self.lower = []
        self.higher = []

    def addNum(self, num: int) -> None:
        if len(self.median) == 2:
            minn, maxx = min(self.median), max(self.median)
            if num > maxx:
                num, maxx = maxx, num
            elif num < minn:
                num, minn = minn, num
            heapq.heappush(self.lower, -minn)
            heapq.heappush(self.higher, maxx)
            self.median = [num]
        
        elif not self.median or num > self.median[0]:
            if self.higher and num > heapq.nsmallest(1, self.higher)[0]:
                tmp = heapq.heappop(self.higher)
                heapq.heappush(self.higher, num)
                num = tmp
            self.median.append(num)
        else:
            if self.lower and num < -heapq.nsmallest(1, self.lower)[0]:
                tmp = heapq.heappop(self.lower)
                heapq.heappush(self.lower, -num)
                num = -tmp
            self.median.insert(0, num)

    def findMedian(self) -> float:
        return sum(self.median) / len(self.median)


def execute(operation, data):

    for o, d in zip(operation, data):
        if o == "MedianFinder":
            medianfinder = MedianFinder()
        if o == "addNum":
            print(medianfinder.addNum(d[0]))
        if o == "findMedian":
            print(medianfinder.findMedian())

    return


operation = ["MedianFinder","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian"]
data = [[],[12],[],[10],[],[13],[],[11],[],[5],[],[15],[],[1],[],[11],[],[6],[],[17],[],[14],[],[8],[],[17],[],[6],[],[4],[],[16],[],[8],[],[10],[],[2],[],[12],[],[0],[]]
execute(operation, data)

operation = ["MedianFinder","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian"]
data = [[],[-1],[],[-2],[],[-3],[],[-4],[],[-5],[]]
execute(operation, data)


operation = ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian", "addNum", "addNum", "addNum"]
data = [[], [1], [2], [], [3], [], [5], [10], [9]]
execute(operation, data)