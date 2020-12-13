import math

from ..aoc import Puzzle


class P(Puzzle):
    
    input_delimiter = None
    
    def process_input_data(self, input_data):
        
        min_time, schedule = input_data.split('\n')
        
        self.earliest_departure = int(min_time)
        
        return [int(t) for t in schedule.split(',') if t != 'x']
    
    def _part1(self, input_data):
        
        min_time = self.earliest_departure
        
        next_time = None
        next_bus = None
        for t in input_data:
            n = math.ceil(min_time / t) * t
            if next_time is None or n < next_time:
                next_time = n
                next_bus = t
        
        time_diff = next_time - min_time
        
        return next_bus * time_diff
    
    def _part2(self, input_data):
        
        pass
