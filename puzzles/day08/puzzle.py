from ..aoc import Puzzle


def run_program(input_data):
    
    acc = 0
    ptr = 0
    seen_ptrs = set()
    
    while ptr not in seen_ptrs:
        instruction, value = input_data[ptr]
        seen_ptrs.add(ptr)
        
        if instruction == 'acc':
            acc += value
        
        if instruction == 'jmp':
            ptr += value
        else:
            ptr += 1
    
    return acc


class P(Puzzle):
    
    def process_input_item(self, input_item):
        
        instruction, value = input_item.split(' ')
        value = int(value)
        
        return instruction, value
    
    def _part1(self, input_data):
        
        return run_program(input_data)
    
    def _part2(self, input_data):
        
        pass
