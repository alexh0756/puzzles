def numRescueBoats(people, limit):

    people = sorted(people, reverse=True)

    boats = 0
    while len(people):

        rem = limit - people[0]

        i = len(people)
        while people[i-1] <= rem and i > 1:
            i -= 1

        if i != len(people):
            people.pop(i)
        people.pop(0)
        boats += 1

    return boats

print(f"ans: 2, calc: {numRescueBoats(people=[5,4,2,1], limit=6)}")
print(f"ans: 1, calc: {numRescueBoats(people=[1,2], limit=3)}")
print(f"ans: 3, calc: {numRescueBoats(people=[3,2,2,1], limit=3)}")
print(f"ans: 4, calc: {numRescueBoats(people=[3,5,3,4], limit=5)}")