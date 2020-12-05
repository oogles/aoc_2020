from ..aoc import Puzzle


class P(Puzzle):
    
    input_delimiter = '\n\n'  # individual entries are separated by blank lines
    
    def process_input_item(self, input_item):
        
        data = {}
        for pair in input_item.split():  # split on any whitespace, including newlines
            key, value = pair.split(':')
            data[key] = value
        
        return data
    
    def _part1(self, input_data):
        
        valid_passports = 0
        
        for item in input_data:
            item.pop('cid', None)  # ignore country ID
            
            # Cheat and just ensure there are 7 remaining fields, without
            # actually checking what they are
            num_fields = len(item.keys())
            if num_fields == 7:
                valid_passports += 1
        
        return valid_passports
    
    def _part2(self, input_data):
        
        pass
