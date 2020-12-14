import math

from ..aoc import Puzzle


class P(Puzzle):
    
    input_delimiter = None
    
    def process_input_data(self, input_data):
        
        min_time, schedule = input_data.split('\n')
        
        self.earliest_departure = int(min_time)
        
        return [int(t) if t != 'x' else t for t in schedule.split(',')]
    
    def _part1(self, input_data):
        
        min_time = self.earliest_departure
        
        next_time = None
        next_bus = None
        for t in input_data:
            if t == 'x':
                continue
            
            n = math.ceil(min_time / t) * t
            if next_time is None or n < next_time:
                next_time = n
                next_bus = t
        
        time_diff = next_time - min_time
        
        return next_bus * time_diff
    
    def _part2(self, input_data):
        
        first_bus_id = input_data[0]
        min_t = first_bus_id
        
        # Initially, if the departure times don't line up from the `min_t` time
        # established above, increment it by the first bus ID (skipping the
        # times in between which will never align). The step value will change
        # as more attempts are made so that more invalid times can be skipped.
        step = first_bus_id
        
        for i, bus_id in enumerate(input_data[1:], start=1):
            # Buses without IDs can be skipped
            if bus_id == 'x':
                continue
            
            # The desired departure time is given by `min_t` plus the index of
            # this bus in the schedule. Find the point at which this desired
            # time actually lines up with a valid departure time, indicated by
            # the bus ID being a multiple of it. Keep stepping to the
            # next-possible `min_t` value whenever the times don't align.
            while (min_t + i) % bus_id:
                min_t += step
            
            # The step value for the next bus in the schedule needs to adapt,
            # taking into account the current bus ID
            step *= bus_id
        
        return min_t
