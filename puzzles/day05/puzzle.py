import math

from ..aoc import Puzzle


class P(Puzzle):
    
    def process_input_item(self, input_item):
        
        row_min = 0
        row_max = 127
        col_min = 0
        col_max = 7
        
        for char in input_item:
            if char == 'F':
                row_max -= math.ceil((row_max - row_min) / 2)
            elif char == 'B':
                row_min += math.ceil((row_max - row_min) / 2)
            elif char == 'L':
                col_max -= math.ceil((col_max - col_min) / 2)
            elif char == 'R':
                col_min += math.ceil((col_max - col_min) / 2)
        
        return row_min * 8 + col_min
    
    def _part1(self, input_data):
        
        return max(input_data)
    
    def _part2(self, input_data):
        
        pass
