from collections import defaultdict

from ..aoc import Puzzle


class P(Puzzle):
    
    def process_input_item(self, input_item):
        
        return input_item.split(' = ')
    
    def _part1(self, input_data):
        
        mask = None
        memory = defaultdict(lambda: 0)
        
        for instruction, value in input_data:
            if instruction == 'mask':
                mask = value
            else:
                mem_addr = instruction[4:-1]
                
                # Convert the value to a 0-padded 36-bit binary string, then
                # convert that to a list to support item assignment
                value = list(f'{int(value):0>36b}')
                
                # Apply the current bitmask
                for i, bit in enumerate(mask):
                    if bit in ('1', '0'):
                        value[i] = bit
                
                memory[mem_addr] = int(''.join(value), 2)
        
        return sum(memory.values())
    
    def _part2(self, input_data):
        
        pass
