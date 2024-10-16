





def final_position(commands):
    position = 0
    direction = 0  # 0: right, 1: down, 2: left, 3: up
    for command in commands:
        if command == 'F':
            if direction == 0:  # right
                position += 1
            elif direction == 2:  # left
                position -= 1
        elif command == 'R':
            direction = (direction + 1) % 4
        elif command == 'L':
            direction = (direction - 1) % 4
    return position

def possible_positions(N, commands):
    # Calculate the original final position
    original_position = final_position(commands)
    
    # Set to keep track of unique positions
    unique_positions = {original_position}

    # Try replacing each command with 'F', 'R', and 'L'
    for i in range(N):
        for new_command in 'FRL':
            if commands[i] != new_command:
                new_commands = commands[:i] + new_command + commands[i+1:]
                new_position = final_position(new_commands)
                unique_positions.add(new_position)

    return len(unique_positions)

# Input handling
N = int(input().strip())
commands = input().strip()

# Calculate and print the number of unique positions
result = possible_positions(N, commands)
print(result)

