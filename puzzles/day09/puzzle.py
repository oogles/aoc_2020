import itertools

from ..aoc import Puzzle


class P(Puzzle):
    
    def process_input_item(self, input_item):
        
        return int(input_item)
    
    def _part1(self, input_data):
        
        n = 5 if self.sample else 25
        
        # Start looking at values *following* the n-length preamble
        for i, v in enumerate(input_data[n:]):
            # The value should be the sum of some pair in the preceding n
            # values (noting that the first n values in the data were skipped)
            pool = input_data[i:i + n]
            
            for pair in itertools.permutations(pool, 2):
                if sum(pair) == v:
                    break
            else:
                # The loop did not break, the value is not a sum of any pair
                # of the preceding n values
                return v
        
        return None
    
    def _part2(self, input_data):
        
        pass
