import itertools

from ..aoc import Puzzle


class P(Puzzle):
    
    def process_input_item(self, input_item):
        
        return int(input_item)
    
    def _part1(self, input_data):
        
        for pair in itertools.combinations(input_data, 2):
            if sum(pair) == 2020:
                return pair[0] * pair[1]
    
    def _part2(self, input_data):
        
        for pair in itertools.combinations(input_data, 3):
            if sum(pair) == 2020:
                return pair[0] * pair[1] * pair[2]
