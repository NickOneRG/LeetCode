
def getMinCost(crew_id, job_id):

    crew_id.sort()
    job_id.sort()

    total = 0
    for crew, job in zip(crew_id, job_id):
        total += abs(crew - job)

    return total




def nearlySimilarRectangles(sides):
    asp_ratios = [side[0] / side[1] for side in sides]
    asp_ratios.sort()

    count, cons_count = 0, 1
    cur_ratio = asp_ratios[0]

    for i in range(1, len(asp_ratios)):
        if abs(asp_ratios[i] - cur_ratio) <= 1e-6:
            cons_count += 1
        else:
            count += cons_count * (cons_count - 1) // 2
            cur_ratio, cons_count = asp_ratios[i], 1

    count += cons_count * (cons_count - 1) // 2

    return count


print(nearlySimilarRectangles([[4,8], [15,30], [25,50]]))


if __name__ == '__main__':
    n = int(input())
    s = []
    for i in range(1, n+1):
        s.append(str(i))

    print("".join(s))
