from ..aoc import Puzzle


class P(Puzzle):
    
    def process_input_item(self, input_item):
        
        return int(input_item)
    
    def _part1(self, input_data):
        
        one_jolt_diffs = 0
        three_jolt_diffs = 1  # always a 3-jolt diff from the last adapter to the device
        current_joltage = 0
        for adapter_joltage in sorted(input_data):
            diff = adapter_joltage - current_joltage
            
            if diff == 3:
                three_jolt_diffs += 1
            elif diff == 1:
                one_jolt_diffs += 1
            else:
                raise Exception('Invalid joltage difference!')
            
            current_joltage = adapter_joltage
        
        return one_jolt_diffs * three_jolt_diffs
    
    def _part2(self, input_data):
        
        pass
