

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    N = int(data[0])  
    commands = data[1].strip()  

    possible = set()

    
    def simulate(commands):
        pos = 0
        dir = 0  

        for command in commands:
            match command:
                case 'F':
                    match dir:
                        case 0: pos += 1
                        case 1: pos -= 1
                        case 2: pos -= 1
                        case 3: pos += 1

                case 'R': dir = (dir + 1) % 4
                case 'L': dir = (dir - 1) % 4

        return pos

    possible.add(simulate(commands))

    for i in range(N):
        for comm in 'RL':
            if commands[i] == 'F':
                continue  
            memo = list(commands)
            memo[i] = comm
            possible.add(simulate(memo))

    for i in range(N):
        if commands[i] == 'F':
            for comm in 'RL':
                memo = list(commands)
                memo[i] = comm
                possible.add(simulate(memo))

    print(len(possible))


if __name__ == "__main__":
    main()




