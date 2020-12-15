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
        
        mask = None
        memory = defaultdict(lambda: 0)
        
        for instruction, value in input_data:
            if instruction == 'mask':
                mask = value
            else:
                mem_addr = instruction[4:-1]
                
                # Convert the memory address to a 0-padded 36-bit binary string,
                # then convert that to a list to support item assignment
                mem_addr = list(f'{int(mem_addr):0>36b}')
                
                # Apply the current bitmask, potentially expanding the single
                # memory address into multiple
                mem_addr_list = [mem_addr]
                for i, bit in enumerate(mask):
                    if bit == '1':
                        # Replace the corresponding bit in ALL memory addresses
                        # with 1
                        for addr in mem_addr_list:
                            addr[i] = '1'
                    elif bit == 'X':
                        # Replace the corresponding bit in ALL memory addresses
                        # with 1 and, for each one, create a copy of the address
                        # with the same bit set to 0
                        for addr in mem_addr_list[:]:  # iterate a copy to facilitate appending to the list
                            addr[i] = '1'
                            addr_copy = addr[:]
                            addr_copy[i] = '0'
                            mem_addr_list.append(addr_copy)
                
                for addr in mem_addr_list:
                    addr = int(''.join(addr), 2)
                    memory[addr] = int(value)
        
        return sum(memory.values())
