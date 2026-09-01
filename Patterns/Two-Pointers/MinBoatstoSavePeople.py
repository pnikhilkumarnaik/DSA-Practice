def num_rescue_boats(people, limit):

    people.sort()

    left = 0
    right = len(people) - 1

    boats = 0

    while left <= right:

        if people[left] + people[right] <= limit:
            left += 1

        right -= 1
        boats += 1

    return boats


people = [3, 2, 2, 1]
limit = 3

print(num_rescue_boats(people, limit))