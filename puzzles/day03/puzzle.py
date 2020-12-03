from ..aoc import Puzzle


class P(Puzzle):
    
    def _part1(self, input_data):
        
        map_width = len(input_data[0])
        map_height = len(input_data)
        
        move_right = 3
        move_down = 1
        
        x, y = 0, 0
        num_trees = 0
        
        while y < map_height - 1:
            x += move_right
            y += move_down
            
            # The pattern provided by the `input_data` matrix continues to the
            # "right" infinitely. Thus the square indicated by the x-coordinate
            # can be found using the modulus of that coordinate with the width
            # of the given map area.
            map_square = input_data[y][x % map_width]
            
            if map_square == '#':
                num_trees += 1
        
        return num_trees
    
    def _part2(self, input_data):
        
        pass
