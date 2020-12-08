from ..aoc import Puzzle


def run_program(input_data):
    
    acc = 0
    ptr = 0
    complete = False
    last_ptr = len(input_data) - 1
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
        
        if ptr > last_ptr:
            complete = True
            break
    
    return acc, complete


class P(Puzzle):
    
    def process_input_item(self, input_item):
        
        instruction, value = input_item.split(' ')
        value = int(value)
        
        return instruction, value
    
    def _part1(self, input_data):
        
        acc, complete = run_program(input_data)
        
        return acc
    
    def _part2(self, input_data):
        
        # Locate every "jmp" and "nop" instruction and swap them, one at a time,
        # until the corrupted instruction is found. Nothing like a bit of brute
        # force!
        for i, item in enumerate(input_data):
            instruction, value = item
            
            if instruction == 'acc':
                # "No acc instructions were harmed in the corruption of this boot code"
                continue
            
            # The instruction is either "jmp" or "nop". Take a copy of the
            # instruction list and swap the instruction (jmp -> nop,
            # nop -> jmp).
            input_copy = input_data[:]
            if instruction == 'jmp':
                input_copy[i] = ('nop', value)
            else:
                input_copy[i] = ('jmp', value)
            
            # If the modified program terminates correctly, the corrupted
            # instruction has been rectified
            acc, complete = run_program(input_copy)
            
            if complete:
                return acc
        
        return None
