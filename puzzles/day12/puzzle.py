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
            
            print(x, y)
        
        return abs(x) + abs(y)
    
    def _part2(self, input_data):
        
        pass
