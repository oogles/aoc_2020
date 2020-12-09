import itertools

from ..aoc import Puzzle


def find_bad_value(data, n):
    
    # Start looking at values *following* the n-length preamble
    for i, v in enumerate(data[n:]):
        # The value should be the sum of some pair in the preceding n
        # values (noting that the first n values in the data were skipped)
        pool = data[i:i + n]
        
        for pair in itertools.permutations(pool, 2):
            if sum(pair) == v:
                break
        else:
            # The loop did not break, the value is not a sum of any pair
            # of the preceding n values
            return v, i
    
    return None, None


class P(Puzzle):
    
    def process_input_item(self, input_item):
        
        return int(input_item)
    
    def _part1(self, input_data):
        
        n = 5 if self.sample else 25
        value, index = find_bad_value(input_data, n)
        
        return value
    
    def _part2(self, input_data):
        
        n = 5 if self.sample else 25
        bad_value, bad_index = find_bad_value(input_data, n)
        
        # From the pool of values preceding the bad value, find a contiguous,
        # arbitrary-length series of values that sum to the bad value
        min_index = 0
        max_index = 1
        while max_index < bad_index:
            total = sum(input_data[min_index:max_index])
            
            if total == bad_value:
                break
            elif total > bad_value:
                # The sum got too high, raise the minimum index
                min_index += 1
            else:
                # The sum is too low, raise the maximum index
                max_index += 1
        else:
            raise Exception('Did not find encryption weakness')  # for Justin
        
        value_range = input_data[min_index:max_index]
        min_value = min(value_range)
        max_value = max(value_range)
        
        return min_value + max_value
