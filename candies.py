def candy(ratings) -> int:
    if not ratings:
        return 0
    
    n = len(ratings)

    level = 1
    counter = 1
    state = None
    local_max = ratings[0]
    for i in range(1, n):
        if ratings[i-1] < ratings[i]:
            if state == 'up':
                level += 1
            else:
                level = 2
                state = 'up'
        elif ratings[i-1] > ratings[i]: # creates unlimited slack so can be joined to previous segment
            if state == 'down':
                level += 1
            else:
                level = 1
                local_max = ratings[i-1]
                state = 'down'
            if level >= local_max:
                local_max += 1
                counter += 1
        else: # need to calculate how this affects previous slack
            level = 1
            state = None
        
        counter += level


def candy(ratings) -> int:
    if not ratings:
        return 0
    
    n = len(ratings)

    level = 1
    counter = 1
    state = None
    previous_val = 1
    for i in range(1, n):
        if ratings[i-1] < ratings[i]:
            if state in ('up', None):
                level += 1
            else:
                level = 2
                previous_val = 1
            state = 'up'
        elif ratings[i-1] > ratings[i]: # creates unlimited slack so can be joined to previous segment
            if state in ('down', None):
                level += 1
            else:
                previous_val = level
                level = 1
            state = 'down'
        else: # need to calculate how this affects previous slack
            level = previous_val = 1
            state = None
        # print(f"val: {ratings[i]}, level: {level}, counter: {counter}")
        if level == previous_val and previous_val != 1:
            level += 1

        counter += level


    print(counter)

    return counter

# candy(ratings = [4,2,3,4,1])
candy(ratings = [29,51,87,87,72,12])
candy(ratings = [1,3,2,2,1])
candy(ratings = [1,0,2])
candy(ratings = [1,2,2])
candy(ratings = [1,2,3,2,1,3,1,1])
candy(ratings = [0,1,4,2,1,0,3,2,1,0])

# examples
# 
#     3     4 1 2 3 4
#     o 1 2 3 o 1 2 3
#   2   o 1 2   o 1 2
# 1 o     o 1     o 1
# o         o       o

#           
#     3     2
#   2 o 2   o 
# 1 o   o 1   1 1 
# o       o   o o


#     3     4
#     o       1 2 3 4
#       1 2 3 o 1 2 3
#   2   o 1 2   o 1 2
# 1 o     o 1     o 1
# o         o       o

#1  3  7 10 12 13 17 20 22 23 - original algo
#1  2  4  3  2  1  4  3  2  1 - original
#1  3  6  7  9 13 15 16 19 23 - my algo
#1  2  3  1  2  4  2  1  3  4
[0, 1, 4, 2, 1, 0, 3, 2, 1, 0]