from ..aoc import Puzzle


class P(Puzzle):
    
    def process_input_item(self, input_item):
        
        instruction = input_item[0]
        value = input_item[1:]
        
        return instruction, int(value)
    
    def _part1(self, input_data):
        
        directions = 'NESW'
        
        # The ferry starts facing east
        current_direction = 'E'
        x = 0
        y = 0
        
        for instruction, value in input_data:
            if instruction in ('L', 'R'):
                # Turn the ferry. Convert the value in degrees into the number
                # of 90-degree increments it represents.
                steps = value // 90
                if instruction == 'L':
                    steps *= -1
                
                # Convert that number of steps into an index of the 4-item
                # character array of cardinal directions, by first adding it to
                # the current direction's index in that array
                steps += directions.index(current_direction)
                index = steps % 4
                
                current_direction = directions[index]
                continue
            elif instruction == 'F':
                move_direction = current_direction
            else:
                move_direction = instruction
            
            if move_direction == 'N':
                y += value
            elif move_direction == 'E':
                x += value
            elif move_direction == 'S':
                y -= value
            elif move_direction == 'W':
                x -= value
        
        return abs(x) + abs(y)
    
    def _part2(self, input_data):
        
        ferry_x = 0
        ferry_y = 0
        
        # The waypoint starts 10 units east and 1 unit north relative to the ferry
        waypoint_x = 10
        waypoint_y = 1
        
        for instruction, value in input_data:
            if instruction in ('L', 'R'):
                # Rotate the waypoint. Convert the value in degrees into the
                # number of 90-degree increments it represents.
                steps = value // 90
                
                multiplier = -1 if instruction == 'L' else 1
                
                for i in range(steps):
                    x, y = waypoint_x, waypoint_y
                    
                    # The northward/southward coordinates become the
                    # eastward/westward coordinates, depending on which way
                    # the waypoint is being rotated
                    if y >= 0:
                        waypoint_x = y * multiplier
                    else:
                        waypoint_x = y * multiplier
                    
                    # The eastward/westward coordinates become the
                    # northward/southward coordinates, depending on which way
                    # the waypoint is being rotated
                    if x >= 0:
                        waypoint_y = x * multiplier * -1
                    else:
                        waypoint_y = x * multiplier * -1
            elif instruction == 'F':
                # Move the ferry to the waypoint the given number of times
                ferry_x += (waypoint_x * value)
                ferry_y += (waypoint_y * value)
            elif instruction == 'N':
                waypoint_y += value
            elif instruction == 'E':
                waypoint_x += value
            elif instruction == 'S':
                waypoint_y -= value
            elif instruction == 'W':
                waypoint_x -= value
        
        return abs(ferry_x) + abs(ferry_y)
