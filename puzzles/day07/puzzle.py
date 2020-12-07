from ..aoc import Puzzle


class P(Puzzle):
    
    input_delimiter = None  # don't auto-process into a list
    
    def process_input_data(self, input_data):
        
        bags = {}
        
        for input_item in input_data.split('\n'):
            outer_colour, contents = input_item.split(' bags contain ')
            contents = contents.strip('.')  # lose the full stop
            
            inner_bags = {}
            for item in contents.split(', '):
                if item == 'no other bags':
                    continue
                
                quantity, colour = item.split(' ', 1)
                colour, _ = colour.rsplit(' ', 1)  # lose the trailing "bag"/"bags"
                inner_bags[colour] = int(quantity)
            
            bags[outer_colour] = inner_bags
        
        return bags
    
    def _part1(self, input_data):
        
        def can_contain_shiny_gold(bags):
            
            if 'shiny gold' in bags:
                return True
            
            for inner_colour in bags:
                can_contain = can_contain_shiny_gold(input_data[inner_colour])
                if can_contain:
                    return True
            
            return False
        
        valid_bags = []
        for outer_colour, inner_bags in input_data.items():
            if outer_colour == 'shiny gold':
                # Not interested in what "shiny gold" holds, only what holds *it*
                continue
            
            if can_contain_shiny_gold(inner_bags):
                valid_bags.append(outer_colour)
        
        return len(valid_bags)
    
    def _part2(self, input_data):
        
        pass
