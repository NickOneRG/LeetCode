

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    N = int(data[0])
    segments = []

    for i in range(1, N + 1):
        a, b = map(int, data[i].split())
        segments.append((a, b))

    segments.sort(key=lambda x: (x[0], -x[1]))

    non_i_count = 0
    act_seg = [] 

    for a, b in segments:
        while act_seg and act_seg[-1][1] < b:
            act_seg.pop()

        if not act_seg or act_seg[-1][1] < b:
            non_i_count += 1

        act_seg.append((a, b))

    print(non_i_count)


if __name__ == "__main__":
    main()


def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    N = int(data[0])
    segments = []

    for i in range(1, N + 1):
        a, b = map(int, data[i].split())
        segments.append((a, b))

    segments.sort()

    non_i_count = 0
    curr_max_b = -1  

    for a, b in segments:
        if b < curr_max_b:
            continue
        else:
            non_i_count += 1
            curr_max_b = b  

    print(non_i_count)

if __name__ == "__main__":
    main()
