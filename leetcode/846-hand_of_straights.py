from collections import Counter

def isNStraightHand(hand, groupSize):

    if len(hand) % groupSize != 0:
        return False
    
    counts = Counter(hand)

    while counts:
        minn = min(counts.keys())
        for i in range(minn, minn+groupSize):
            if i in counts:
                counts[i] -= 1
                if counts[i] < 1:
                    counts.pop(i)
            else:
                return False

    return True

print(isNStraightHand(hand = [1,2,3,6,2,3,4,7,8], groupSize = 3))
print(isNStraightHand(hand = [1,2,3,4,5], groupSize = 4))