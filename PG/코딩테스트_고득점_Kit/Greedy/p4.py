def solution(people, limit):
    people.sort()

    boat_for_two = 0
    l, r = 0, len(people) - 1
    while r > l:
        if people[l] + people[r] <= limit:
            l += 1
            boat_for_two +=1
        r -= 1

    return len(people) - boat_for_two
