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
        
        # Add the device joltage (being the highest adapter joltage + 3) to the
        # list so only chains that are valid right up to the device are counted
        device_joltage = max(input_data) + 3
        input_data.append(device_joltage)
        
        # Recursively traverse the list in sorted order, following every valid
        # chain of adapters
        input_data.sort()
        
        # Cache results of each index, as each one will be called A LOT
        cache = {}
        
        def next(index, joltage):
            
            valid_chains = 0
            
            while True:
                index += 1
                next_joltage = input_data[index]
                
                if next_joltage > joltage + 3:
                    break
                
                # It falls within the valid joltage range, so we've either
                # reached the device (count a complete chain), or we need to
                # proceed to the next adapter
                if next_joltage == device_joltage:
                    return 1
                
                try:
                    result = cache[index]
                except KeyError:
                    result = next(index, next_joltage)
                    cache[index] = result
                
                valid_chains += result
            
            return valid_chains
        
        return next(-1, 0)
